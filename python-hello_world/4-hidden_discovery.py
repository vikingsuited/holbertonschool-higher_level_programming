#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # Modulun içindəki bütün adları alırıq
    names = dir(hidden_4)
    
    # Adları əlifba sırası ilə düzürük
    names.sort()
    
    for name in names:
        # Yalnız "__" ilə başlamayan adları çap edirik
        if not name.startswith("__"):
            print(name)
