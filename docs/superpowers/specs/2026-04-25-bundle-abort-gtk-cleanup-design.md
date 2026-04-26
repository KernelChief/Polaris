# Design: Bundle Halt on Failure + GTK Doc Cleanup

**Date:** 2026-04-25
**Branch:** fix/boxbuddy-libglvnd-gles-dep (or new branch)

---

## Problem

1. **Bundle silent-continue:** When any step in `run_bundle` fails (e.g. a `dnf_deps` install), `_run_action_sequence` calls `on_abort=on_done`, which fires `after()` — advancing the bundle to the next feature silently. The user sees no failure indication and the bundle completes as if nothing went wrong.

2. **GTK doc leftover:** `docs/learnings/GTK.md` is a learning doc from the old GTK3 era, now irrelevant since the UI was fully migrated to PySide6 (Qt6) in commit `692fa9d`. Its entry in `docs/INDEX.md` is also stale.

---

## Approach

**Approach A** — Thread `on_abort` through `_run_action_sequence`.

No new concepts: follows the exact pattern already established by `_run_helper`'s `on_abort` parameter.

---

## Changes

### 1. `_run_action_sequence` — add `on_abort` parameter

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

`on_abort` is forwarded directly to each `_run_helper` call. When any step fails, `on_abort` fires and the sequence short-circuits (no remaining steps run).

### 2. `run_bundle` — supply a dedicated abort handler

```python
def on_abort_bundle():
    self._set_busy(fid, False)
    self._append_log(f"== Bundle aborted: failed during '{f['name']}' ==\n")
    self.refresh_states()
    self._toggle_buttons(True)
    self.bundle_running = False

self._run_action_sequence(actions, on_done=after, on_abort=on_abort_bundle)
```

On failure: busy spinner clears for the failed feature, a clear abort message appears in the log, all buttons re-enable, and `bundle_running` resets to `False`. No subsequent features in the bundle are attempted.

### 3. `on_click` single-install — make `on_abort` explicit

Currently `on_click` calls `_run_action_sequence(actions, on_done=lambda: self._done(fid))` with no `on_abort`. Since `_run_action_sequence` now passes `on_abort=None` to `_run_helper` (instead of `on_done`), single-install abort would leave the row stuck in busy state. Fix: pass `on_abort=lambda: self._done(fid)` explicitly.

```python
self._run_action_sequence(
    actions,
    on_done=lambda: self._done(fid),
    on_abort=lambda: self._done(fid),
)
```

### 4. GTK doc cleanup

- Delete `docs/learnings/GTK.md`
- Remove its row from `docs/INDEX.md`
- No source code changes needed — `src/polaris` and `src/polaris-helper` are already fully GTK-free

---

## Out of Scope

- Partial bundle resume (retry failed features)
- Per-feature failure badges in the UI row
- Any changes to `_run_helper` or `HelperRunner`

---

## QA Checklist

- [ ] Single install: a feature with `dnf_deps` that fails DNF → row returns to idle, log shows failure
- [ ] Single install: a feature with `dnf_deps` that succeeds → Flatpak installs normally
- [ ] Bundle: first feature fails → bundle halts, log shows abort message, buttons re-enable
- [ ] Bundle: feature without `dnf_deps` fails → bundle halts identically
- [ ] Bundle: all features succeed → "Bundle complete" message appears as before
- [ ] `docs/learnings/GTK.md` no longer exists
- [ ] `docs/INDEX.md` no longer references GTK.md
