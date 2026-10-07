"""Task 2: simulate streaming by polling a feed on a timer."""
import argparse
import time
from datetime import datetime
import pandas as pd

from .fetch import fetch_feed, geojson_to_df

def filter_unseen(df: pd.DataFrame, seen: set) -> pd.DataFrame:
    """Return only rows whose (id, updated) pair is not in `seen`.

    Add the new pairs to `seen` (modify the set in place).
    """
    ...
    new_rows = []

    for _, row in df.iterrows():

        key = (row["id"], row["updated"])

        if key not in seen:
            seen.add(key)
            new_rows.append(row)

    return pd.DataFrame(new_rows, columns=df.columns)


def run_stream(feed: str, interval_s: int, duration_s: int, out_path: str) -> None:
    """Poll `feed` every `interval_s` seconds for `duration_s` seconds.

    Each poll: fetch, parse, keep unseen rows, append them to `out_path`
    as JSON lines, and print e.g. "[14:02:11] 3 new / 12 fetched".
    A failed poll must not stop the loop.
    """
    ...
    seen = set()

    start_time = time.time()

    while time.time() - start_time < duration_s:

        try:
            payload = fetch_feed(feed)

            df = geojson_to_df(payload)

            new_df = filter_unseen(df, seen)

            if not new_df.empty:

                with open(out_path, "a", encoding="utf-8") as f:

                    new_df.to_json(
                        f,
                        orient="records",
                        lines=True
                    )

            current_time = datetime.now().strftime("%H:%M:%S")

            print(
                f"[{current_time}] "
                f"{len(new_df)} new / {len(df)} fetched"
            )

        except Exception as e:

            print(f"Stream error: {e}")

        time.sleep(interval_s)



def main() -> None:
    """argparse: --feed (default all_hour), --interval (60), --duration (2400),
    --out (data/stream/stream.jsonl), then call run_stream."""
    ...
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--feed",
        default="all_hour"
    )

    parser.add_argument(
        "--interval",
        type=int,
        default=60
    )

    parser.add_argument(
        "--duration",
                type=int,
        default=2400
    )

    parser.add_argument(
        "--out",
        default="data/stream/stream.jsonl"
    )

    args = parser.parse_args()

    run_stream(
        args.feed,
        args.interval,
        args.duration,
        args.out
    )




if __name__ == "__main__":
    main()
