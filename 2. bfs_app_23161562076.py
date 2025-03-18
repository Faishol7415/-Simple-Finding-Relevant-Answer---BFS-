from collections import deque

def bfs_faq_search(faq_graph, query):
    queue = deque([(query, [query])])  # (node_saat_ini, jalur_ke_node)
    visited = set()

    while queue:
        current, path = queue.popleft()
        if current in faq_graph.get("answers", {}):
            return faq_graph["answers"][current]  # Kembalikan jawaban jika ditemukan
        if current not in visited:
            visited.add(current)
            for neighbor in faq_graph.get(current, []):
                queue.append((neighbor, path + [neighbor]))
    
    return "Jawaban tidak ditemukan."

# Contoh penggunaan
faq_graph = {
    "Apa itu AI?": ["Machine Learning", "Deep Learning"],
    "Machine Learning": ["Supervised Learning", "Unsupervised Learning"],
    "Deep Learning": ["Neural Networks"],
    "answers": {
        "Neural Networks": "Neural Networks adalah model AI yang terinspirasi dari otak manusia.",
        "Supervised Learning": "Supervised Learning menggunakan data berlabel untuk pelatihan."
    }
}

query = "Apa itu AI?"
answer = bfs_faq_search(faq_graph, query)
print("Jawaban yang Relevan:", answer)
