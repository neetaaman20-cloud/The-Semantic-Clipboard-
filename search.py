import sys
from core import search_clips

def main():
    if len(sys.argv) < 2:
        print("Usage: python search.py 'your search query'")
        return

    query = " ".join(sys.argv[1:])
    results = search_clips(query)

    print(f"\n🔍 Top matches for: '{query}'\n" + "-"*30)
    
    for doc in results['documents'][0]:
        print(f"📌 {doc}\n" + "-"*30)

if __name__ == "__main__":
    main()