import os
import argparse
from aicontrol import SchemaGenerator

def create_directories(schema, rootdir):
    """Create directories based on the schema."""
    for line in schema.split("\n"):
        # Clean the directory line
        line = line.strip()

        # Skip empty lines
        if not line:
            continue

        # Remove trailing "/" and calculate depth
        line = line.rstrip("/")
        depth = line.count("  ")

        # Build the full directory path
        dir_path = os.path.join(rootdir, *line.split("/"))

        # Create the directory if it doesn't exist
        os.makedirs(dir_path, exist_ok=True)

def main():
    # Set up the CLI argument parser
    parser = argparse.ArgumentParser(
        description="Nebula One CLI: Generate and create directory schemas based on natural language prompts."
    )
    parser.add_argument(
        "command", type=str, choices=["generateschema"],
        help="Command to execute. Currently supports 'generateschema'."
    )
    parser.add_argument(
        "prompt", type=str,
        help="Natural language description for the directory structure."
    )
    parser.add_argument(
        "--rootdir", type=str, default=os.getcwd(),
        help="Root directory where the folders will be created (default: current directory)."
    )

    # Parse arguments
    args = parser.parse_args()

    if args.command == "generateschema":
        # Initialize SchemaGenerator
        schema_gen = SchemaGenerator(project_id="nebulaone-444719")

        # Generate the schema
        print("Generating schema...")
        schema = schema_gen.generate_schema(args.prompt)

        # Display the generated schema
        print("\nGenerated Schema:")
        print(schema)

        # Create directories in the specified root directory
        create_directories(schema, args.rootdir)
        print(f"\nDirectories successfully created in: {args.rootdir}")

if __name__ == "__main__":
    main()
