# Bundle Halt on Failure + GTK Doc Cleanup — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make `run_bundle` halt immediately on any step failure with a clear log message, and remove the stale GTK learning doc.

**Architecture:** Thread `on_abort` through `_run_action_sequence` so callers can supply a distinct failure handler. `run_bundle` supplies one that logs the abort, clears busy state, re-enables buttons, and resets `bundle_running`. No changes to `_run_helper` or `HelperRunner`.

**Tech Stack:** PySide6 (Qt6), Python 3, single-file app `src/polaris`

---

> **Note:** The `on_click` single-install `on_abort` fix (spec Section 3) was already committed in `d872679`. Tasks below cover only what remains.

---

### Task 1: Thread `on_abort` through `_run_action_sequence`

**Files:**
- Modify: `src/polaris:975-985`

- [ ] **Step 1: Open `src/polaris` and locate `_run_action_sequence` at line 975**

Current code:
```python
def _run_action_sequence(self, actions: list, on_done=None):
    queue = [a for a in actions if a]

    def step(i=0):
        if i >= len(queue):
            if on_done:
                on_done()
            return
        self._run_helper(queue[i], on_done=lambda: step(i + 1), on_abort=on_done)

    step()
```

- [ ] **Step 2: Replace with the `on_abort`-aware version**

```python
def _run_action_sequence(self, actions: list, on_done=None, on_abort=None):
    queue = [a for a in actions if a]

    def step(i=0):
        if i >= len(queue):
            if on_done:
                on_done()
            return
        self._run_helper(queue[i], on_done=lambda: step(i + 1), on_abort=on_abort)

    step()
```

The only changes are: `on_abort=None` added to the signature, and `on_abort=on_done` → `on_abort=on_abort` on the `_run_helper` call. When any step fails, `on_abort` fires and no further steps run.

- [ ] **Step 3: Verify no other call sites of `_run_action_sequence` are broken**

Run:
```bash
grep -n "_run_action_sequence" src/polaris
```

Expected output — exactly these two lines:
```
956:        self._run_action_sequence(actions, on_done=lambda: self._done(fid), on_abort=lambda: self._done(fid))
1025:        self._run_action_sequence(actions, on_done=after)
```

Line 956 already passes `on_abort` explicitly (committed in `d872679`) — safe.
Line 1025 is `run_bundle` — `on_abort` will default to `None` until Task 2. That is intentional: Task 2 supplies the real handler.

- [ ] **Step 4: Commit**

```bash
git add src/polaris
git commit -m "refactor: thread on_abort through _run_action_sequence

Callers can now supply a distinct failure handler. Forwards on_abort
directly to _run_helper instead of falling back to on_done, so success
and failure paths are no longer conflated.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

### Task 2: Supply bundle abort handler in `run_bundle`

**Files:**
- Modify: `src/polaris:1018-1025`

- [ ] **Step 1: Locate the `step` inner function inside `run_bundle` (around line 1002)**

Current code in the inner loop (lines 1018–1025):
```python
            self._set_busy(fid, True, "Installing…")

            def after():
                self._set_busy(fid, False)
                self.refresh_states()
                step(i + 1)

            self._run_action_sequence(actions, on_done=after)
```

- [ ] **Step 2: Add `on_abort_bundle` and pass it to `_run_action_sequence`**

Replace with:
```python
            self._set_busy(fid, True, "Installing…")

            def after():
                self._set_busy(fid, False)
                self.refresh_states()
                step(i + 1)

            def on_abort_bundle():
                self._set_busy(fid, False)
                self._append_log(f"== Bundle aborted: failed during '{f['name']}' ==\n")
                self.refresh_states()
                self._toggle_buttons(True)
                self.bundle_running = False

            self._run_action_sequence(actions, on_done=after, on_abort=on_abort_bundle)
```

`on_abort_bundle` captures `fid` and `f` from the enclosing `step` scope — both are local parameters so closure is safe. On any failure: clears the busy spinner for the failed feature, appends an abort line to the log, refreshes row states, re-enables all buttons, and resets `bundle_running`.

- [ ] **Step 3: Commit**

```bash
git add src/polaris
git commit -m "fix: halt bundle immediately on step failure

When any action in run_bundle fails, the bundle now stops, clears the
busy state for the failed feature, logs a clear abort message, and
re-enables all buttons. Previously, failure silently advanced to the
next bundle item.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

### Task 3: Remove stale GTK learning doc

**Files:**
- Delete: `docs/learnings/GTK.md`
- Modify: `docs/INDEX.md:19`

- [ ] **Step 1: Delete the GTK doc**

```bash
rm "docs/learnings/GTK.md"
```

- [ ] **Step 2: Remove the GTK row from `docs/INDEX.md`**

Current `docs/INDEX.md` table:
```markdown
| **GTK UI** | `docs/learnings/GTK.md` | ~400 |
| **Qt 5/6** | `docs/learnings/QT.md` | ~500 |
```

Remove the `GTK UI` row so the table becomes:
```markdown
| **Qt 5/6** | `docs/learnings/QT.md` | ~500 |
```

Also update the `Last Updated` line at the bottom to today's date:
```markdown
**Last Updated**: 2026-04-25
```

- [ ] **Step 3: Verify the file is gone and index is clean**

```bash
ls docs/learnings/
grep -n "GTK" docs/INDEX.md
```

Expected: `GTK.md` not listed in `docs/learnings/`. `grep` returns no output.

- [ ] **Step 4: Commit**

```bash
git add docs/learnings/GTK.md docs/INDEX.md
git commit -m "docs: remove stale GTK learning doc

The UI was fully migrated to PySide6 (Qt6) in 692fa9d. GTK.md is no
longer relevant and its INDEX.md entry has been removed."
```

---

## QA Checklist (manual, post-implementation)

- [ ] Single install: a feature with `dnf_deps` that fails DNF → row returns to idle, log shows failure
- [ ] Single install: a feature with `dnf_deps` that succeeds → Flatpak installs normally
- [ ] Bundle: any feature fails → bundle halts, log shows `== Bundle aborted: failed during '...' ==`, buttons re-enable
- [ ] Bundle: feature without `dnf_deps` fails → bundle halts identically
- [ ] Bundle: all features succeed → `== Bundle complete: ... ==` message appears as before
- [ ] `docs/learnings/GTK.md` no longer exists
- [ ] `docs/INDEX.md` no longer references GTK.md
