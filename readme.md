# Mini hotloader
### Give it directory path to watch and command to run after modification in files in that directory.

## How to use it ?

```python
pip install -r requirements.txt
```
run the script
```python
python watch.py [args]
```
## Arguements are 
**--file**: Path to text files containing all the directories path to watch.

**--dir**: Path to single directory to watch.

**--cmd**: Command to run after any modification in watching directory

**-r**: Watch subdirectory or not default is False

*Note:* If both --file and --dir is given --dir will be prioratized

## Example

```python
python watch.py --file="/path/to/file/all_paths.txt"
```

Here "all_path.txt" file is used to get all the directories

*all_path.txt* may look like
```text
/path/to/dir1
/path/to/dir2
/path/to/dir3
```
```python
python watch.py --dir="/path/to/dir"
```
It will just watch *dir* directory.