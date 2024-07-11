from spirit import state, simulation, io
from pathlib import Path


def run_llg(cfg_file: Path, input_image_path: Path, benchmark_output_path: Path):
    """Run the LLG method.

    Args:
        cfg_file (Path): Path to the spirit config file
        input_image_path (Path): Path to the input image
        benchmark_output_path (Path) : Path of the file to which to append the benchmark output
    """

    assert cfg_file.exists()
    assert input_image_path.exists()

    with state.State(str(cfg_file), quiet=False) as p_state:
        io.image_read(p_state, input_image_path.as_posix())

        run_info = simulation.start(
            p_state, simulation.METHOD_LLG, simulation.SOLVER_VP
        )

        with open(benchmark_output_path, "a") as f:
            print(f"{run_info.total_iterations = }", file=f)
            print(f"{run_info.total_walltime = }s", file=f)
            print(f"{run_info.max_torque = }", file=f)
            print(f"{run_info.total_ips = }", file=f)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("cfg_file", type=Path, help="Path to the spirit config file")
    parser.add_argument(
        "input_image_path", type=Path, help="Path to the input image ovf file"
    )
    parser.add_argument(
        "benchmark_output_path",
        type=Path,
        help="Path of the file to which to append the benchmark output",
    )

    args = parser.parse_args()

    cfg_file = args.cfg_file
    input_image_path = args.input_image_path
    benchmark_output_path = args.benchmark_output_path

    run_llg(cfg_file, input_image_path, benchmark_output_path)
