import sys


def ft_stream_management() -> None:
    sys.stdout.write("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    sys.stdout.write("\nInput Stream active. Enter archivist ID: ")
    sys.stdout.flush()
    archivist_id = sys.stdin.readline().strip()

    sys.stdout.write("Input Stream active. Enter status report: ")
    sys.stdout.flush()
    report_status = sys.stdin.readline().strip()

    sys.stdout.write("\n[STANDARD] Archive status from {}: {}".format(
            archivist_id, report_status))
    sys.stderr.write("\n[ALERT] System diagnostic: Communication \
channels verified")
    sys.stdout.write("\n[STANDARD] Data transmission complete")

    sys.stdout.write("\n\nThree-channel communication test successful.")


if __name__ == "__main__":
    ft_stream_management()
