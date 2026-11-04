# Post kit

Renders New Narrative carousel slides (1080×1350) and stories (1080×1920) from the
design system artifact (tokens v2): Inter display type in mixed weights, approved
colour combinations, one combination per carousel, colour logo lockup only on charcoal
at display size, story text inside the 250 / 340px safe zones.

Fonts come from npm `@fontsource/*` packages unpacked into `../fonts` (see `kit.py`).
Run `python3 posts.py p05 p06 …` to render into `out/`.
