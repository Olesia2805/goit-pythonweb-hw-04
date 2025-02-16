import asyncio
import logging
import argparse
import shutil
from aiopath import AsyncPath

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


async def read_folder(file_source_path: AsyncPath, file_output_path: AsyncPath):
    """Recursively reads files and causes them to be copied."""
    tasks = []
    async for path in file_source_path.glob("**/*"):
        if await AsyncPath.is_file(path):
            tasks.append(copy_file(path, file_output_path))

    results = await asyncio.gather(*tasks)
    logging.info(f"Processed {len(results)} files.")
    return results


async def copy_file(file_path: str, file_output_path: AsyncPath):
    """Copies a file to the appropriate folder by extension."""
    try:
        extension = file_path.suffix[1:] or "unknown"
        target_path = file_output_path / extension
        await target_path.mkdir(parents=True, exist_ok=True)
        new_file_path = target_path / file_path.name
        await asyncio.to_thread(shutil.copy, file_path, new_file_path)
        logging.info(f"Copied: {file_path.name} -> {new_file_path}")
    except Exception as e:
        logging.error(f"Error copying file {file_path}: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Asynchronously sort files by extension"
    )
    parser.add_argument(
        "-s",
        "--source",
        const="source",
        nargs="?",
        type=str,
        help="Path to the source folder",
    )
    parser.add_argument(
        "-o",
        "--output",
        const="output",
        nargs="?",
        type=str,
        help="Path to the output folder",
    )
    args = parser.parse_args()

    source_folder = AsyncPath(args.source)
    output_folder = AsyncPath(args.output)

    asyncio.run(read_folder(source_folder, output_folder))


if __name__ == "__main__":
    main()
