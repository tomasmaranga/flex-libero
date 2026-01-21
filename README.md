**IMPORTANT**: please use this command to clone

```
git clone --recurse-submodules https://github.com/tomasmaranga/flex-libero.git
```

this is because LIBERO is a submodule, so to clone it as well you need the flag

```bash
# env
conda env create -f environment.yml
conda activate flex-libero

# deps
pip install -r third_party/LIBERO/requirements.txt
pip install -e third_party/LIBERO
python third_party/LIBERO/benchmark_scripts/download_libero_datasets.py
```
