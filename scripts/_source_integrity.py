"""Verify the imported text-source snapshot without executing it."""
import hashlib
from pathlib import Path
from _stylepacks import ROOT, inside, read_json


def verify_sources(root=ROOT):
    root=Path(root)
    common=root/'vendor/lemo-opuscar'
    manifest=read_json(common/'manifest.json')
    checked=0
    def verify(folder, relative, expected):
        nonlocal checked
        path=inside(folder,relative)
        actual=hashlib.sha256(path.read_bytes()).hexdigest()
        if actual!=expected:
            raise ValueError(f"source hash mismatch: {path}")
        checked+=1
    for item in manifest['common_files']:
        verify(common,item['path'],item['sha256'])
    for style in manifest['styles']:
        folder=root/'styles'/style['id']
        origin=style['origin']
        verify(folder,'STYLE.upstream.md',origin['style_sha256'])
        verify(folder,'DEMO.md',origin['demo_sha256'])
        verify(folder,'style.upstream.json',origin['metadata_sha256'])
        if (folder/'LICENSE').read_bytes()!=(common/'LICENSE').read_bytes():
            raise ValueError(f"upstream license mismatch: {folder}")
        for item in style['files']:
            verify(folder,item['path'],item['sha256'])
    return dict(status='passed',files=checked,styles=len(manifest['styles']),revision=manifest['revision'],scope='source-integrity-only')
