# Stock footage and stills (stand-ins, D9/D20)

Graded stand-in footage used on the canvas boards and previews. Mood only: never captioned as a Cybertronix product (D20).
Sources: Pexels lab-arm clips (free licence) and an Unsplash factory photo by Shavr IK (free licence).
Grade: brightness -10, contrast +18, saturation 55%, slight blue lift (docs/design.md §6).

`blob-ids.json` maps the asset ids used in `design/boards/gen.py` (dict `B`, old canvas) to these files.
A new canvas needs these files re-uploaded as assets; then replace the ids in `B` with the new ones.
For previews, set `BLOB_MAP` to a JSON of `{id: path}` built from `blob-ids.json`
(see `design/boards/preview.cjs`).
