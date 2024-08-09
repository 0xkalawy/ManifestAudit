# ManifestAudit

**ManifestAudit** is a Python tool designed to analyze and extract crucial information from AndroidManifest.xml files. This tool helps developers and security analysts to inspect Android applications by extracting activities, permissions, namespaces, and other key elements.

## Features

- **Extract Activities**: List all activities within the AndroidManifest.xml file, with an option to filter those that are exported or contain an intent-filter.
- **Custom Permissions**: Retrieve all custom permissions defined by the developer.
- **Uses Permissions**: Display all the permissions required by the application to run.
- **Namespace Detection**: Automatically detect and display the Android namespace used in the XML file.
- **Dump Mode**: Extract all possible data, providing a comprehensive overview of the AndroidManifest.xml file.
- **Colored Output**: Easily distinguish different types of data with colored terminal output.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/MohamedWagdy7/ManifestAudit.git
   cd ManifestAudit
   ```

## Usage

Run the tool using Python:

```bash
python main.py -f path/to/AndroidManifest.xml [options]
```

### Command-Line Options

- `-f`, `--file`: Path to the AndroidManifest.xml file (required).
- `-o`, `--output`: Output file (only text file is supported).
- `--activities`: Print only activities.
- `--get-namespace`: Print only the namespace.
- `--namespace`: Provide the namespace of the file (if not set, the tool will determine it automatically).
- `--custom-permissions`: Print only the permissions defined by the developer.
- `--uses-permissions`: Print the permissions needed for the application to run.
- `--dump`: Dump the whole file and extract all possible data.

### Example Commands

- **Extract Activities**:

  ```bash
  python main.py -f path/to/AndroidManifest.xml --activities
  ```

- **Print Namespace**:

  ```bash
  python main.py -f path/to/AndroidManifest.xml --get-namespace
  ```

- **Dump All Data**:
  ```bash
  python main.py -f path/to/AndroidManifest.xml --dump
  ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue if you have any suggestions or improvements.

## Contact

For any questions or inquiries, you can reach out to [wagdym014@gmail.com](mailto:wagdym014@gmail.com).
