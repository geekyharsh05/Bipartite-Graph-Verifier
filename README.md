# Bipartite Graph Verification

## Usage

Run the script with the following command:

```bash
python src/main.py --nodes N
```

## Arguments

- --nodes N: Specifies the number of nodes in the graph.

## Functionality

### 1. `is_bipartite(graph)`

This function checks if a given graph is bipartite.

#### Parameters:

- `graph` (dict): An adjacency list representation of the graph where keys represent nodes, and values are lists of neighbors.

#### Returns:

- `bool`: True if the graph is bipartite, False otherwise.

### 2. `main()`

The main function acts as a command-line interface for bipartite graph verification.

- Parses command-line arguments using `argparse`.
- Accepts user input for the neighbors of each node to construct the graph.
- Calls `is_bipartite` to check if the graph is bipartite.
- Prints the result.


## Demonstration

```bash
python bipartite.py --nodes 4
Enter neighbors of node 0 (space-separated): 1 3
Enter neighbors of node 1 (space-separated): 0 2
Enter neighbors of node 2 (space-separated): 1 3
Enter neighbors of node 3 (space-separated): 0 2
The graph is bipartite.
```

## Note

- An empty graph is considered **bipartite** by default.
- The script uses a depth-first search (DFS) approach to check for bipartiteness.
- The result is printed, indicating whether the graph is bipartite or not

## Author

**Author Name** &nbsp; : &nbsp; Harsh Vardhan Pandey <br>
**Author URI** &nbsp; &nbsp; &nbsp; : &nbsp; [www.aboutharsh.vercel.app](https://aboutharsh.vercel.app/) <br>
**GitHub URI** &nbsp; &nbsp; &nbsp; : &nbsp; [geekyharsh05](https://github.com/geekyharsh05)

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)