import glob
import re
import os 

# Quick and dirty script to process Rmd into a passable md document.

INPUT_DIR="raw_docs/"

OUTPUT_DIR="docs/"

def process_rmd(path: str):
    with open(path, "r") as f:
        rmd_text = f.read()
    
    # Get title of page
    title = re.findall('title:\s+"(.*?)"', rmd_text, flags=re.MULTILINE)
    
    if len(title) != 1:
        raise RuntimeError(f"Couldn't parse title for '{path}'")
    else:
        title = " ".join(e.capitalize() if not e.isupper() else e for e in title[0].replace("-", " ").split())

    # Strip header and replace with title as a H1 header
    rmd_text = re.sub("^---(.*?)^---", f"#{title}", rmd_text, count=1, flags=re.MULTILINE | re.DOTALL)

    # Strip R setup chunk
    rmd_text = re.sub("^```{r setup.*?^```", "", rmd_text, flags=re.MULTILINE | re.DOTALL)

    # Replace R chunks with R syntax highlighting.
    rmd_text = re.sub("{r .*?}", "r", rmd_text)

    # Replace R image calls with normal markdown.
    rmd_text = re.sub("^```.*?knitr::include_graphics\((.*?)\).*?^```", "[](\g<1>)", rmd_text, flags=re.MULTILINE | re.DOTALL)

    out_fname = os.path.split(path)[1]
    out_fname_noext,_ = os.path.splitext(out_fname)

    out_path = os.path.join(OUTPUT_DIR, f"{out_fname_noext}.md")

    with open(out_path, "w") as f:
        f.write(rmd_text)
 

if __name__ == "__main__":
    # Get Rmd
    all_rmd = glob.glob(os.path.join(INPUT_DIR, "*.Rmd"))

    for rmd in all_rmd:
        print(f"Processing {rmd}...")
        process_rmd(rmd)