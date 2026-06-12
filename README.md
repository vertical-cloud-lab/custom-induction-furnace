# custom-induction-furnace

Custom Induction Furnace project - Documentation and resources for building and operating an induction furnace.

## Documentation

Relevant documentation is stored in the Box shared folder. To download and access the documentation locally:

```bash
# Download documentation from Box
python download_box_docs.py

# For more options:
python download_box_docs.py --info
```

Downloaded files will be saved to the `docs/` directory.

### Box Shared Link
- **URL**: https://byu.box.com/s/lh04mmpkhvhy4vtokpm4sol711xycrph
- **Contents**: Project documentation, design files, and operational guides
- **Access**: Publicly accessible shared folder

### Download Options

#### Option 1: Automatic Download (Recommended)
```bash
python download_box_docs.py
```

#### Option 2: Manual Download
Visit the Box link above and download files directly to the `docs/` directory.

#### Option 3: Using Box API (with credentials)
```bash
export BOX_CLIENT_ID="your_client_id"
export BOX_CLIENT_SECRET="your_client_secret"
python download_box_docs.py --use-api
```

For Box API credentials, see: https://developer.box.com/guides/authentication/oauth2/

## Related Issues
- Issue #2: Attempt download of relevant docs from box
- Issue #1: Manuscript Notes - Paper about hardware design and operation