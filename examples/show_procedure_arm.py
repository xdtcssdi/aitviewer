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
        # Display in the viewer.
    v = Viewer()
    v.run_animations = False
    pi = 3.1415926
    c = [149 / 255, 85 / 255, 149 / 255, 1]
    c1 = [100 / 255, 255 / 255, 149 / 255, 1]
    start_degree = 0
    end_degree = 90
    frames_count = 7
    interval = (end_degree - start_degree) / frames_count
    for i in range(frames_count+1):
        c[-1] = 0.5 if i > 0 and i <frames_count else 1

        frame = np.zeros((1, 23*3))
        frame[:, 17*3+2] = -(start_degree + i * interval) * pi/ 180
        seq_amass = SMPLSequence.pose(poses=frame,
            poses_root=np.zeros((1, 3)),
            color=tuple(c),
            # name="pose",
            show_joint_angles=True,
        )
        v.scene.add(seq_amass)


        c1[-1] = 0.5 if i > 0 and i <frames_count else 1

        frame2 = np.zeros((1, 23*3))
        frame2[:, 15*3+2] = -(start_degree + i * interval) * pi/ 180
        seq_amass2 = SMPLSequence.pose(poses=frame2,
            poses_root=np.zeros((1, 3)),
            color=tuple(c1),
            # name="pose",
            show_joint_angles=True,
        )
        seq_amass2.position = (0, 0, 0)
        v.scene.add(seq_amass2)
    v.run()
