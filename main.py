import yaml
import argparse
import os

def generate_mermaid(data):
    """Convert YAML data to Mermaid code with professional shape formatting."""
    lines = ["graph TD"]
    
    # 1. Define Nodes with specific geometric shapes based on type
    for node in data['nodes']:
        n_id = node['id']
        n_name = node['name']
        n_type = node['type']
        
        if n_type == "Ingestion":
            # Hexagon - represents data entry/ingestion
            lines.append(f"    {n_id}{{{{ {n_name} }}}}")
        elif n_type == "Storage":
            # Cylinder - represents databases/storage
            lines.append(f"    {n_id}[({n_name})]")
        elif n_type == "Processing":
            # Rhombus/Diamond - represents processing logic or decisions
            lines.append(f"    {n_id}{{{ {n_name} }}}")
        else:
            # Standard rectangle for other types
            lines.append(f"    {n_id}[{n_name}]")

    # 2. Add Relationships (Flows)
    for flow in data['flows']:
        lines.append(f"    {flow['from']} -->| {flow['label']} | {flow['to']}")

    return "\n".join(lines)

def main():
    # Setup CLI to make the tool professional for terminal usage
    parser = argparse.ArgumentParser(description="BigData-Flow-Architect: Infrastructure as Code for Diagrams")
    parser.add_argument("-i", "--input", default="architecture.yaml", help="Path to input YAML file")
    parser.add_argument("-o", "--output", default="output/diagram.md", help="Path to save the Markdown output")
    
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"❌ Error: Configuration file '{args.input}' not found.")
        return

    try:
        with open(args.input, 'r') as file:
            config = yaml.safe_load(file)
            
        mermaid_code = generate_mermaid(config)
        
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(args.output), exist_ok=True)
        
        with open(args.output, 'w') as out:
            out.write(f"# Project: {config.get('project', 'Big Data Architecture')}\n\n")
            out.write("Generated using [BigData-Flow-Architect]\n\n")
            out.write(f"```mermaid\n{mermaid_code}\n```")
        
        print(f"🚀 Success! Diagram generated for project: {config.get('project')}")
        print(f"📂 Location: {args.output}")
        print("\n--- Preview of Mermaid Code ---")
        print(mermaid_code)

    except Exception as e:
        print(f"💥 An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()