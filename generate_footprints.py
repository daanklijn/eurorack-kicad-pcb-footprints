from pathlib import Path

hps = [1,2,4,6,8,10,12,14,16,18,20,21,22,28,42]
widths = [5,9.8,20.0,30.0,40.3,50.5,60.6,70.8,80.9,91.3,101.3,106.3,111.4,141.9,213.0]

for hp, width in zip(hps,widths):
    Path(f'Eurorack_PCB_{hp}HP.kicad_mod').write_text(
    f"""
    (module Eurorack_PCB_{hp}HP (layer F.Cu) (tedit 6117BFB2)
      (fp_text reference REF** (at 0 0.5) (layer F.SilkS)
        (effects (font (size 1 1) (thickness 0.15)))
      )
      (fp_text value Eurorack_PCB_{hp}HP (at 0 -0.5) (layer F.SilkS)
        (effects (font (size 1 1) (thickness 0.15)))
      )
      (fp_line (start 0 0) (end {width} 0) (layer Edge.Cuts) (width 0.12))
      (fp_line (start 0 0) (end 0 110) (layer Edge.Cuts) (width 0.12))
      (fp_line (start 0 110) (end {width} 110) (layer Edge.Cuts) (width 0.12))
      (fp_line (start {width} 0) (end {width} 110) (layer Edge.Cuts) (width 0.12))
    )
    """
    )


