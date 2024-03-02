def solution(edges):
    in_edges, out_edges = [0 for _ in range(1000000)], [0 for _ in range(1000000)]
    max_edge = 0

    for edge_from, edge_to in edges:
        in_edges[edge_to] += 1
        out_edges[edge_from] += 1
        max_edge = max(max_edge, edge_from, edge_to)
    
    start_node = 0
    graph_cnt = [0, 0, 0]
    DOUGHNUT, STICK, EIGHT = 0, 1, 2

    for i in range(1, max_edge + 1):
        # in 간선이 없으면 생성한 정점
        if in_edges[i] == 0 and out_edges[i] > 1:
            start_node = i
        # out 간선이 2이면 8자 모양 그래프
        elif out_edges[i] == 2:
            graph_cnt[EIGHT] += 1
        # 막대 모양 그래프
        elif out_edges[i] == 0:
            graph_cnt[STICK] += 1
    graph_cnt[DOUGHNUT] = out_edges[start_node] - graph_cnt[EIGHT] - graph_cnt[STICK]

    return [start_node, graph_cnt[DOUGHNUT], graph_cnt[STICK], graph_cnt[EIGHT]]