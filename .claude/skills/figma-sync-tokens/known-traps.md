# Known Traps & Resolutions — figma-sync-tokens

| Trap / Behavior | Root Cause & Resolution |
|---|---|
| **Expired REST Token Warning** | Expected behavior. Don't spend time renewing it — all variable extraction runs through the Desktop Bridge plugin. |
| **Silent Bridge Disconnection** | The Desktop Bridge disconnects whenever someone edits the Figma file. Re-run the plugin and run `figma_get_status` (`probe: true`). |
| `Variable.key` missing | Not exposed by `figma_get_variables`. Read it via `figma_execute` using `getLocalVariablesAsync()`. |
| `figma_get_library_variables` timeout | A file cannot query itself via team-library APIs. Use local execution routes via `figma_execute`. |
| Stale reads / aggressive cache | `refreshCache` requires dead REST tokens. Use `figma_execute` to query live node state instead. |
| Page cap at 100 | API requests silently cap at 100 items. Paginate (e.g. 221 color tokens require 3 paged requests). |
| Duplicate counts in `variable_names` | The cached list inflates total count (~3194 vs ~1642 real). Always count per collection via `figma_execute`. |
| Renamed vs. recreated tokens | Renames retain publish keys; delete-and-recreate generates new keys. Re-verify keys after changes. |
