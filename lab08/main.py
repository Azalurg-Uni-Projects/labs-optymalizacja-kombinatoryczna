# Implement algorithm CPM
# https://www.geeksforgeeks.org/software-engineering-critical-path-method/
import random
import time
from typing import Dict, List
import networkx as nx
import matplotlib.pyplot as plt


class Task:
    def __init__(self, id: int, duration: int, predecessors: List[int]):
        self.id = id
        self.duration = duration
        self.predecessors = predecessors
        self.EFT = 0
        self.LFT = 0
        self.EST = 0
        self.LST = 0
        self.on_critical_path = False
        self.float = 0

    def __str__(self):
        return f"{self.id}-{self.predecessors}"


class Graph:
    def __init__(self, tasks: Dict[int, Task]):
        self.tasks = tasks
        self.eft = 0

    def compute_earliest_times(self):
        for task in self.tasks.values():
            if not task.predecessors:
                task.EST = 0
                task.EFT = task.duration
            else:
                predecessor_efts = [self.tasks[predecessor_id].EFT for predecessor_id in task.predecessors]
                task.EST = max(predecessor_efts)
                task.EFT = task.EST + task.duration
            if task.EFT > self.eft:
                self.eft = task.EFT

    def compute_latest_times(self):
        tasks = list(self.tasks.values())[::-1]
        for task in tasks:
            successors = [t for t in tasks if task.id in t.predecessors]
            if not successors:
                task.LFT = self.eft
                task.LST = task.LFT - task.duration
            else:
                successor_lsts = [self.tasks[successor.id].LST for successor in successors]
                task.LFT = min(successor_lsts)
                task.LST = task.LFT - task.duration

    def compute_float(self):
        for task in self.tasks.values():
            task.float = task.LST - task.EST
            if task.float == 0:
                task.on_critical_path = True

    def draw(self):
        # utworzenie pustego grafu
        G = nx.DiGraph()

        # dodanie wierzchołków do grafu
        G.add_node("start", duration=0, EFT=0, LFT=0, EST=0, LST=0, float=0)
        for task in self.tasks.values():
            G.add_node(task.id, duration=task.duration, EFT=task.EFT, LFT=task.LFT, EST=task.EST, LST=task.LST,
                       float=task.float)
        G.add_node("finish", duration=0, EFT=0, LFT=0, EST=0, LST=0, float=0)

        # dodanie krawędzi do grafu
        for task in self.tasks.values():
            if not task.predecessors:
                G.add_edge("start", task.id)
            for predecessor in task.predecessors:
                G.add_edge(predecessor, task.id)
            successors = [successor.id for successor in self.tasks.values() if task.id in successor.predecessors]
            if not successors:
                G.add_edge(task.id, "finish")

        # liczenie pozycji wierzchołków
        pos = {"start": (0, 0)}
        tasks_coppy = self.tasks.copy()
        rotation = 1
        while tasks_coppy:
            to_include = []
            for task in tasks_coppy:
                if not tasks_coppy[task].predecessors:
                    to_include.append(tasks_coppy[task])
            for task in to_include:
                tasks_coppy.pop(task.id)

            id_coppy = [task.id for task in tasks_coppy.values()]
            for task in tasks_coppy:
                for predecessor in tasks_coppy[task].predecessors:
                    if predecessor not in id_coppy:
                        tasks_coppy[task].predecessors.remove(predecessor)

            def f(n):
                output = []
                for i in range(n):
                    output.append(i - n / 2)
                return output

            amount = f(len(to_include))
            for task in to_include:
                pos[task.id] = (rotation, amount.pop(-1))
            rotation += 2

        pos["finish"] = (rotation, 0)

        # rysowanie scieżki krytycznej
        critical_path_edges = ["start"]
        critical_path_edges += [task.id for task in self.tasks.values() if task.on_critical_path]
        critical_path_edges += ["finish"]

        for v in range(len(critical_path_edges) - 1):
            nx.draw_networkx_edges(G, pos, edgelist=[(critical_path_edges[v], critical_path_edges[v + 1])], width=8, alpha=0.5, edge_color='r')

        # rysowanie grafu
        nx.draw(G, pos)

        # dodanie etykiet
        labels = {}
        for node in G.nodes:
            if node == "start" or node == "finish":
                labels[node] = node
            else:
                labels[node] = f"EST: {G.nodes[node]['EST']} D: {G.nodes[node]['duration']} EFT: {G.nodes[node]['EFT']}\n id: {node} \n LST: {G.nodes[node]['LST']} float: {G.nodes[node]['float']} LFT: {G.nodes[node]['LFT']}"
        nx.draw_networkx_labels(G, pos, labels, font_size=16, bbox=dict(facecolor='white', alpha=0.35))
        plt.show()

#         --------------------

        class Machine:
            def __init__(self):
                self.tasks = []
                self.time = 0

        #Todo: zaimplementować algorytm

        plan = [Machine()]
        tasks_list = list(self.tasks.values())
        tasks_list.sort(key=lambda x: x.EFT)

        while tasks_list:
            l = len(plan) - 1
            added = False
            for task in tasks_list:
                if task.EST >= plan[l].time:
                    plan[l].tasks.append(task)
                    plan[l].time += task.duration
                    tasks_list.remove(task)
                    added = True
                    break
            if not added:
                plan.append(Machine())

        max_end_time = max([task.EFT for task in self.tasks.values()])

        # Create a figure and an axis
        fig, ax = plt.subplots()

        # Iterate through the tasks and create a horizontal bar for each one
        for i, machine in enumerate(plan):
            timeline = 0
            for task in machine.tasks:
                timeline += task.duration
                if timeline < task.EST:
                    timeline = task.EST
                ax.barh(i, task.duration, left=timeline - task.duration, height=0.5, color="#0086b3", edgecolor="black")
                ax.text(timeline - task.duration / 2, i, f"id: {task.id} | t:{task.duration}", ha="center", va="center", color="white")

        # Set the y-axis labels to the task IDs
        ax.set_yticks([i for i in range(len(plan))])
        ax.set_yticklabels([i for i in range(len(plan))])

        # Set the x-axis limits to the maximum end time
        ax.set_xlim(0, max_end_time + 1)

        # Show the plot
        plt.show()


tasks = {
    1: Task(1, 6, []),
    2: Task(2, 4, []),
    3: Task(3, 3, [1]),
    4: Task(4, 4, [2]),
    5: Task(5, 3, [2]),
    6: Task(6, 10, []),
    7: Task(7, 3, [5, 6]),
    8: Task(8, 2, [3, 4])
}

# tasks = {
#     1: Task(1, 3, []),
#     2: Task(2, 8, []),
#     3: Task(3, 2, []),
#     4: Task(4, 2, [1]),
#     5: Task(5, 4, [1]),
#     6: Task(6, 6, [2]),
#     7: Task(7, 9, [2]),
#     8: Task(8, 2, [4]),
#     9: Task(9, 1, [2, 5, 6]),
#     10: Task(10, 2, [2, 5, 6]),
#     11: Task(11, 1, [7]),
#     12: Task(12, 2, [7]),
#     13: Task(13, 6, [8, 9]),
#     14: Task(14, 5, [10, 11]),
#     15: Task(15, 9, [10, 11]),
#     16: Task(16, 6, [10, 11]),
#     17: Task(17, 2, [12]),
#     18: Task(18, 5, [13, 14]),
#     19: Task(19, 3, [16, 17]),
# }

graph = Graph(tasks)
graph.compute_earliest_times()
graph.compute_latest_times()
graph.compute_float()
graph.draw()
