#include <iostream>
#include <map>
#include <cmath>

using namespace std;


struct Cell {
    int i_, j_;
    Cell () {}
    Cell (int i, int j) {
        i_ = i;
        j_ = j;
    }
};

int n_case = 1;
Cell dim;
typedef pair<int, Cell> Path;
int final_state;

bool is_visited(int state, Cell cell) {
    int i = cell.i_;
    int j = cell.j_;
    int col = dim.j_;
    int cell_bit_mask_pos = 1 << (i * col + j);

    return state & cell_bit_mask_pos;
}

bool is_valid_destination(Cell ori_cell, Cell dest_cell) {
    int ori_i = ori_cell.i_;
    int ori_j = ori_cell.j_;
    int dest_i = dest_cell.i_;
    int dest_j = dest_cell.j_;

    if (ori_i == dest_i) {
        return false;
    }
    else if (ori_j == dest_j) {
        return false;
    }
    else if ((ori_i - ori_j) == (dest_i - dest_j)){
        return false;
    }
    else if ((ori_i + ori_j) == (dest_i + dest_j)){
        return false;
    }
    else {
        return true;
    }
}

int get_state_with_new_cell(int state, Cell cell) {
    // include new cell into state
    int i = cell.i_;
    int j = cell.j_;
    int col = dim.j_;
    int cell_bit_mask_pos = 1 << (i * col + j);

    return state | cell_bit_mask_pos;
}

int get_state_without_current_cell(int state, Cell cell) {
    // exclude cell from state
    int i = cell.i_;
    int j = cell.j_;
    int col = dim.j_;
    int cell_bit_mask_pos = 1 << (i * col + j);

    return state ^ cell_bit_mask_pos;
}

void get_path(map<int, Cell> paths[]) {
    int r = dim.i_;
    int c = dim.j_;
    int max_steps = r * c;
    int step_ptr = max_steps;
    Cell path[max_steps];
    // using the first cell seen to compute the path
    int current_state = final_state;
    Cell current_cell = paths[max_steps][current_state];
    path[step_ptr] = current_cell;
    for (int s = max_steps - 1; s > 0; s--) {
        current_state = get_state_without_current_cell(current_state, current_cell);
        current_cell = paths[s][current_state];
        path[s] = current_cell;
    }

    for (int i = 1; i <= max_steps; i++) {
        Cell cell = path[i];
        cout << (cell.i_ + 1) << ' ' << (cell.j_ + 1) << endl;
    }
}

void path_search(int r, int c) {
    // init
    dim.i_ = r;
    dim.j_ = c;
    int max_steps = r * c;
    final_state = pow(2, r * c) - 1;
    map<int, Cell> paths[max_steps + 1];
    int starting_state = 1;
    paths[1].insert(Path(starting_state, Cell(0, 0)));

    // walk through the matrix
    for (int step_used = 1; step_used < max_steps; step_used++) {
        map<int, Cell> paths_with_n_step = paths[step_used];
        // get all current states that reachable by exactly n step
        for (map<int, Cell>::iterator itr = paths_with_n_step.begin();
             itr != paths_with_n_step.end();
             itr++) {
            // find possible cells and try to walk into that cell
            int current_state = itr->first;
            Cell current_cell = itr->second;
            for (int i = 0; i < dim.i_; i++) {
                for (int j = 0; j < dim.j_; j++) {
                    Cell dest_cell(i, j);
                    if (is_valid_destination(current_cell, dest_cell)
                        && !is_visited(current_state, dest_cell)) {
                        int new_state = get_state_with_new_cell(current_state, dest_cell);
                        paths[step_used + 1].insert(Path(new_state, dest_cell));
                    }
                }
            }
        }
    }

    // get possible path
    map<int, Cell> paths_at_last_step = paths[max_steps];
    if (paths_at_last_step.find(final_state) != paths_at_last_step.end()) {
        cout << "Case #" << n_case << ": POSSIBLE" << endl;
        get_path(paths);
    } else {
        cout << "Case #" << n_case << ": IMPOSSIBLE" << endl;
    }
    n_case++;
}


int main(int argc, const char * argv[]) {
    int n, r, c;
    scanf("%i", &n);
    for (int _ = 0; _ < n; _++) {
        scanf("%i %i", &r, &c);
        path_search(r, c);
    }
    return 0;
}
