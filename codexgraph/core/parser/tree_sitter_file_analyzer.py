
from pathlib import Path
from tree_sitter_const import LANG_GRAMMARS
import subprocess
from tree_sitter import Language

# 默认构建输出
BUILD_DIR = Path('.tree_sitter_build')
LIB_PATH = BUILD_DIR / 'my-languages.so'

def ensure_language_lib(langs=list({LANG_GRAMMARS.keys()})):
    BUILD_DIR.mkdir(exist_ok=True)
    if not LIB_PATH.exists():
        print(f"Building Tree-sitter languages for: {langs}")
        repo_dir=BUILD_DIR / "repos"
        repo_dir.mkdir(exist_ok=True)
        clone_paths = []
        for lang in langs:
            repo=langs.get(lang)
            if not repo:
                continue
            else:
                lang_repo_path= repo_dir / "tree-sitter-" + lang
                if not lang_repo_path.exists():
                    print(f"Cloning {repo} into {lang_repo_path}")
                    subprocess.run(["git", "clone", repo, str(lang_repo_path)]) 
                clone_paths.append(str(lang_repo_path))
        Language.build_library(
            #output path
            str(LIB_PATH),
            #Repository paths
            clone_paths
        )
        print(f"Built Tree-sitter languages at {LIB_PATH} completed.")
    else:
        print(f"usring existing Tree-sitter language library at {LIB_PATH}.")
    
    languages = {}
    for lang in langs:
        try:
            languages[lang] = Language(str(LIB_PATH), lang)
        except Exception as e:
            print(f"Error loading language {lang}: {e}")
    return languages

class InfraFileAnalyzer:
    def __init__(self):
        pass
    

def analyze_file(path:str langs=None):
    p=Path(path)
    if not p.exists():
        raise FileNotFoundError()
    #detect language
    lang=detect_language_from_extension(p)
    if not lang:
        raise ValueError(f'Can not detect language by file extension from {p.suffix}')
    langs_to_build=[lang]
    language=ensure_language_lib(langs_to_build)
    