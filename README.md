# EmptyDirectoryDelete

The emptydirectorydelete script is a command-line tool that allows you to remove empty folders from a specified directory. This can be useful when you want to clean up your file system and get rid of unnecessary empty directories.

## Prerequisites

Before using this script, ensure that you have the following:

- Python 3.x installed on your system
- Basic familiarity with running scripts from the command line

## Usage

To use the script, follow these steps:

1. Download or copy the `main.py` file to your local machine.
2. Open a command prompt or terminal window.
3. Navigate to the directory where the `main.py` file is located.
4. Run the script using the following command:

   ```
   python main.py <directory>
   ```

   Replace `<directory>` with the path to the directory from which you want to delete empty folders.

   **Example:**

   ```
   python main.py /path/to/directory
   ```

   This will execute the script and remove any empty folders found within the specified directory.

   **Note:** The script will not delete non-empty folders or their contents.

## Acknowledgments

This script was developed using Python and utilizes the `os` and `argparse` libraries.

## Disclaimer

Please use this script with caution and ensure that you have a backup of your data before running it. Deleting folders can permanently remove files and data. The script is provided as-is, without any warranty or guarantee. The author shall not be held responsible for any loss or damage caused by the usage of this script.

## License

This script is licensed under the [MIT License](https://opensource.org/licenses/MIT). Please see the `LICENSE` file for more details.
