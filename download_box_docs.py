#!/usr/bin/env python3
"""
Script to download documentation from Box shared folder.

This script downloads files from the Box shared link:
https://byu.box.com/s/lh04mmpkhvhy4vtokpm4sol711xycrph

The files are saved to the `docs/` directory.

Usage:
    python download_box_docs.py [--output-dir docs] [--shared-link-id lh04mmpkhvhy4vtokpm4sol711xycrph]

Note: This script requires either:
1. Public access to the Box shared link (downloads via web interface)
2. Box API credentials (CLIENT_ID and CLIENT_SECRET environment variables)
   for authenticated API access
3. Selenium or Playwright for browser-based download (for JavaScript-rendered content)
"""

import os
import sys
import argparse
import json
import subprocess
import re
from pathlib import Path
from typing import Optional


def check_if_html(file_path: str) -> bool:
    """Check if a downloaded file is actually HTML instead of a real file."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read(1000)
            return '<!DOCTYPE' in content or '<html' in content
    except:
        return False


def download_via_curl(
    shared_link: str, output_dir: str = "docs"
) -> bool:
    """
    Attempt to download files from Box shared link using curl.
    
    Args:
        shared_link: The Box shared link URL
        output_dir: Directory to save files
        
    Returns:
        True if download was successful, False otherwise
    """
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    try:
        print(f"Attempting to download from: {shared_link}")
        print(f"Saving to: {output_dir}")
        
        # Try downloading with curl following redirects
        # Use -J to save with the remote filename, -L to follow redirects
        output_file = f"{output_dir}/box_files"
        cmd = [
            "curl", "-L", "-J",
            "-o", output_file,
            "--max-time", "30",
            shared_link
        ]
        
        result = subprocess.run(cmd, capture_output=True, timeout=35)
        
        if result.returncode == 0:
            # Find the actual output file (curl may rename it)
            output_path = Path(output_file)
            
            # Check if curl renamed the file (with extension)
            if not output_path.exists():
                # Look for files matching the pattern
                parent_dir = output_path.parent
                pattern = output_path.name
                matches = list(parent_dir.glob(f"{pattern}*"))
                if matches:
                    output_path = matches[0]
            
            if output_path.exists() and output_path.stat().st_size > 0:
                # Check if it's actually an HTML file (Box web interface)
                if check_if_html(str(output_path)):
                    print(f"✗ Downloaded file appears to be HTML (Box web interface)")
                    print(f"  The Box link requires JavaScript to render.")
                    output_path.unlink()
                    return False
                
                # Check if it's a zip file
                if str(output_path).endswith('.zip'):
                    print(f"✓ Downloaded zip file to {output_path}")
                    print(f"  Extract with: unzip {output_path}")
                else:
                    print(f"✓ Downloaded files to {output_path}")
                
                return True
        
        return False
        
    except subprocess.TimeoutExpired:
        print(f"✗ Download timed out (>30 seconds)")
        return False
    except Exception as e:
        print(f"✗ Error downloading: {e}")
        return False


def download_via_box_api(
    shared_link: str,
    client_id: Optional[str] = None,
    client_secret: Optional[str] = None,
    output_dir: str = "docs"
) -> bool:
    """
    Download files from Box shared link using Box API.
    
    Requires Box API credentials (CLIENT_ID and CLIENT_SECRET).
    These can be set as environment variables or passed as arguments.
    
    Args:
        shared_link: The Box shared link URL
        client_id: Box API Client ID
        client_secret: Box API Client Secret
        output_dir: Directory to save files
        
    Returns:
        True if download was successful, False otherwise
    """
    client_id = client_id or os.environ.get("BOX_CLIENT_ID")
    client_secret = client_secret or os.environ.get("BOX_CLIENT_SECRET")
    
    if not client_id or not client_secret:
        print("✗ Box API credentials not provided.")
        print("  Set BOX_CLIENT_ID and BOX_CLIENT_SECRET environment variables")
        print("  or pass them as arguments: --client-id and --client-secret")
        return False
    
    try:
        from boxsdk import Client
        from boxsdk.auth.oauth2 import OAuth2
        
        auth = OAuth2(client_id, client_secret)
        client = Client(auth)
        
        # Get the shared item from the shared link
        # This requires the shared_link_password if the link is password protected
        shared_item = client.shared_items.get(shared_link)
        
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # Download files
        print(f"✓ Connected to Box API")
        print(f"  Item type: {shared_item.type}")
        
        if shared_item.type == "folder":
            print(f"  Folder name: {shared_item.name}")
            print(f"  Item count: {len(list(shared_item.get_items()))}")
            
            # Download all files from the shared folder
            for item in shared_item.get_items():
                print(f"  Downloading: {item.name}")
                with open(f"{output_dir}/{item.name}", "wb") as f:
                    item.download_to(f)
        else:
            print(f"  File name: {shared_item.name}")
            with open(f"{output_dir}/{shared_item.name}", "wb") as f:
                shared_item.download_to(f)
        
        print(f"✓ Download complete!")
        return True
        
    except Exception as e:
        print(f"✗ Error downloading via Box API: {e}")
        return False


def print_info():
    """Print information about the Box shared link."""
    shared_link = "https://byu.box.com/s/lh04mmpkhvhy4vtokpm4sol711xycrph"
    print("\n=== Box Documentation Download ===")
    print(f"\nShared Link: {shared_link}")
    print("\nOptions to download:")
    print("1. Use Box API (requires credentials): python download_box_docs.py --use-api")
    print("2. Manual browser download: Visit the shared link above")
    print("\nFor Box API credentials, see:")
    print("  https://developer.box.com/guides/authentication/oauth2/")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Download documentation from Box shared folder"
    )
    parser.add_argument(
        "--output-dir",
        default="docs",
        help="Output directory for downloaded files (default: docs)"
    )
    parser.add_argument(
        "--shared-link",
        default="https://byu.box.com/s/lh04mmpkhvhy4vtokpm4sol711xycrph",
        help="Box shared link URL"
    )
    parser.add_argument(
        "--use-api",
        action="store_true",
        help="Use Box API instead of curl"
    )
    parser.add_argument(
        "--client-id",
        help="Box API Client ID (or set BOX_CLIENT_ID env var)"
    )
    parser.add_argument(
        "--client-secret",
        help="Box API Client Secret (or set BOX_CLIENT_SECRET env var)"
    )
    parser.add_argument(
        "--info",
        action="store_true",
        help="Show information about the Box link and download options"
    )
    
    args = parser.parse_args()
    
    if args.info:
        print_info()
        return 0
    
    try:
        if args.use_api:
            success = download_via_box_api(
                args.shared_link,
                args.client_id,
                args.client_secret,
                args.output_dir
            )
        else:
            success = download_via_curl(args.shared_link, args.output_dir)
        
        if not success:
            print("\n⚠ Automatic download failed.")
            print("\nAlternative options:")
            print("1. Use Box API with proper credentials:")
            print("   python download_box_docs.py --use-api --client-id YOUR_ID --client-secret YOUR_SECRET")
            print("2. Visit and download manually:")
            print(f"   {args.shared_link}")
            print("3. Save downloaded files to the docs/ directory")
            print("4. Run --info for more help:")
            print("   python download_box_docs.py --info")
            return 1
        
        return 0
        
    except KeyboardInterrupt:
        print("\n✗ Download interrupted by user")
        return 130
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())

