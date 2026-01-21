import os
from libero.libero import benchmark, get_libero_path
from libero.libero.envs import OffScreenRenderEnv

def main():
    os.environ.setdefault("MUJOCO_GL", "egl")

    b = benchmark.get_benchmark_dict()["libero_10"]()
    t = b.get_task(0)

    bddl = os.path.join(get_libero_path("bddl_files"), t.problem_folder, t.bddl_file)

    env = OffScreenRenderEnv(bddl_file_name=bddl, camera_widths=64, camera_heights=64)
    env.reset()
    for _ in range(2):
        env.step([0.0] * 7)
    env.close()

if __name__ == "__main__":
    main()
