"""
Copyright (C) 2022  ETH Zurich, Manuel Kaufmann, Velko Vechev, Dario Mylonopoulos

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import os

import numpy as np
import sys
sys.path.append(".")
from aitviewer.viewer import Viewer
from aitviewer.configuration import CONFIG as C
C.smplx_models = 'models/'
from aitviewer.renderables.point_clouds import PointClouds
from aitviewer.renderables.smpl import SMPLSequence
from aitviewer.viewer import Viewer

if __name__ == "__main__":
    # Load an AMASS sequence and make sure it's sampled at 60 fps. This automatically loads the SMPL-H model.
    # We set transparency to 0.5 and render the joint coordinates systems.
    c = (149 / 255, 85 / 255, 149 / 255, 0.5)
    seq_amass = SMPLSequence.pose(poses=np.zeros((100, 23 *3)),
        poses_root=np.zeros((100, 3)),
        color=c,
        name="pose",
        show_joint_angles=True,
    )

    # Display in the viewer.
    v = Viewer()
    v.run_animations = False

    v.scene.add(seq_amass)
    v.run()
