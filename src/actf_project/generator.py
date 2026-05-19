"""CAD generator module for ACTF project.

This file holds the core CAD generation functions previously in
the top-level script. Keeping logic here makes the project
importable and easier to test.
"""
from __future__ import annotations

from pathlib import Path
import cadquery as cq

OUT_DIR = Path.cwd() / "output"
OUT_DIR.mkdir(exist_ok=True)


def exoskeleton_shell() -> cq.Workplane:
    """Create a robust outer armor shell with shoulder and chest plates."""
    torso = (
        cq.Workplane("XY")
        .ellipse(95, 65)
        .extrude(220)
        .faces(">Z")
        .workplane()
        .transformed(offset=(0, 0, 0))
        .ellipse(70, 45)
        .cutBlind(-170)
    )

    shoulder_left = (
        cq.Workplane("YZ")
        .center(55, 165)
        .ellipse(38, 30)
        .extrude(95)
        .translate((-47, 0, 0))
    )
    shoulder_right = shoulder_left.mirror("YZ")

    rib_guard = (
        cq.Workplane("XY")
        .workplane(offset=95)
        .rect(150, 120)
        .extrude(8)
        .edges("|Z")
        .fillet(6)
    )

    return torso.union(shoulder_left).union(shoulder_right).union(rib_guard)


def endoskeleton_core() -> cq.Workplane:
    """Create modular internal frame and organ bay structure."""
    spine = cq.Workplane("XZ").rect(22, 190).extrude(22).translate((0, 0, 95))

    pelvis = (
        cq.Workplane("XY")
        .ellipse(55, 35)
        .extrude(26)
        .translate((0, 0, 15))
    )

    organ_bay = (
        cq.Workplane("XY")
        .workplane(offset=95)
        .rect(80, 60)
        .extrude(90)
        .faces(">Z")
        .workplane()
        .rect(62, 42)
        .cutBlind(-70)
    )

    shoulder_link_left = (
        cq.Workplane("YZ")
        .center(52, 165)
        .circle(14)
        .extrude(60)
        .translate((-30, 0, 0))
    )
    shoulder_link_right = shoulder_link_left.mirror("YZ")

    return spine.union(pelvis).union(organ_bay).union(shoulder_link_left).union(shoulder_link_right)


def full_body_concept() -> cq.Assembly:
    """Assemble exoskeleton + endoskeleton modules with offset for visualization."""
    exo = exoskeleton_shell()
    endo = endoskeleton_core().translate((0, 0, 8))

    asm = cq.Assembly(name="ACTF_full_body")
    asm.add(exo, name="exoskeleton", color=cq.Color(0.1, 0.15, 0.2, 0.55))
    asm.add(endo, name="endoskeleton", color=cq.Color(0.75, 0.75, 0.8, 1.0))
    return asm


def export_all() -> None:
    exo = exoskeleton_shell()
    endo = endoskeleton_core()
    asm = full_body_concept()

    cq.exporters.export(exo, OUT_DIR / "actf_exoskeleton.step")
    cq.exporters.export(exo, OUT_DIR / "actf_exoskeleton.stl")

    cq.exporters.export(endo, OUT_DIR / "actf_endoskeleton.step")
    cq.exporters.export(endo, OUT_DIR / "actf_endoskeleton.stl")

    asm.save(str(OUT_DIR / "actf_full_body.step"))

