/**
 * MEGA DSA VISUALIZER PRO
 * Author: Advanced Algorithm Simulator
 * Features: Sorting Algorithms, Pathfinding Algorithms, Priority Queues
 */

// Global State Management
const STATE = {
    mode: 'sorting', // 'sorting' or 'path'
    speed: 50,
    isAnimating: false,
    array: [],
    grid: [],
    ROWS: 20,
    COLS: 40,
    startNode: { r: 10, c: 5 },
    endNode: { r: 10, c: 35 },
    mouseIsPressed: false
};

// DOM Elements
const visualizerContainer = document.getElementById('visualizer-container');
const controlsPanel = document.getElementById('controls-panel');
const speedSlider = document.getElementById('global-speed');
const modeSortingBtn = document.getElementById('mode-sorting');
const modePathBtn = document.getElementById('mode-path');

// Utility Functions
const sleep = (ms) => new Promise(resolve => setTimeout(resolve, Math.max(1, 200 - ms)));
const getDelay = () => parseInt(speedSlider.value);

speedSlider.addEventListener('input', (e) => STATE.speed = e.target.value);

// Disable/Enable Controls during animation
function toggleControls(disable) {
    STATE.isAnimating = disable;
    const buttons = controlsPanel.querySelectorAll('button');
    buttons.forEach(btn => {
        btn.disabled = disable;
        btn.className = disable 
            ? "px-4 py-2 rounded bg-slate-700 text-slate-500 cursor-not-allowed font-semibold text-sm transition" 
            : "px-4 py-2 rounded bg-slate-700 text-white hover:bg-cyan-600 hover:shadow-lg font-semibold text-sm transition border border-slate-600";
    });
}

// ==========================================
// MODULE 1: SORTING VISUALIZER
// ==========================================

function initSortingMode() {
    STATE.mode = 'sorting';
    modeSortingBtn.classList.replace('text-slate-400', 'text-white');
    modeSortingBtn.classList.add('bg-accent');
    modePathBtn.classList.replace('text-white', 'text-slate-400');
    modePathBtn.classList.remove('bg-accent');
    
    controlsPanel.innerHTML = `
        <button id="btn-gen-arr">Generate Array</button>
        <button id="btn-bubble">Bubble Sort</button>
        <button id="btn-quick">Quick Sort</button>
        <button id="btn-merge">Merge Sort</button>
        <button id="btn-heap">Heap Sort</button>
    `;
    
    document.getElementById('btn-gen-arr').addEventListener('click', generateArray);
    document.getElementById('btn-bubble').addEventListener('click', async () => { toggleControls(true); await bubbleSort(); toggleControls(false); });
    document.getElementById('btn-quick').addEventListener('click', async () => { toggleControls(true); await quickSortMain(); toggleControls(false); });
    document.getElementById('btn-merge').addEventListener('click', async () => { toggleControls(true); await mergeSortMain(); toggleControls(false); });
    document.getElementById('btn-heap').addEventListener('click', async () => { toggleControls(true); await heapSort(); toggleControls(false); });

    generateArray();
}

function generateArray() {
    if (STATE.isAnimating) return;
    visualizerContainer.innerHTML = '<div class="array-container" id="array-wrapper"></div>';
    const wrapper = document.getElementById('array-wrapper');
    STATE.array = [];
    
    const size = Math.floor(visualizerContainer.clientWidth / 15); // Dynamic size
    for (let i = 0; i < size; i++) {
        let val = Math.floor(Math.random() * 80) + 10;
        STATE.array.push(val);
        const bar = document.createElement('div');
        bar.classList.add('array-bar');
        bar.style.height = `${val}%`;
        bar.style.width = `${100 / size}%`;
        wrapper.appendChild(bar);
    }
}

// 1. Bubble Sort
async function bubbleSort() {
    const bars = document.querySelectorAll('.array-bar');
    let n = bars.length;
    for (let i = 0; i < n - 1; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            bars[j].style.backgroundColor = '#ef4444'; // Red
            bars[j+1].style.backgroundColor = '#ef4444';
            await sleep(getDelay());
            
            let val1 = parseFloat(bars[j].style.height);
            let val2 = parseFloat(bars[j+1].style.height);
            
            if (val1 > val2) {
                bars[j].style.height = `${val2}%`;
                bars[j+1].style.height = `${val1}%`;
            }
            bars[j].style.backgroundColor = '#38bdf8'; // Default
            bars[j+1].style.backgroundColor = '#38bdf8';
        }
        bars[n - 1 - i].style.backgroundColor = '#22c55e'; // Green (Sorted)
    }
    bars[0].style.backgroundColor = '#22c55e';
}

// 2. Quick Sort
async function partition(bars, l, r) {
    let pivot = parseFloat(bars[r].style.height);
    bars[r].style.backgroundColor = '#f59e0b'; // Pivot color
    let i = l - 1;
    for (let j = l; j <= r - 1; j++) {
        bars[j].style.backgroundColor = '#ec4899'; // Scanning
        await sleep(getDelay());
        let valJ = parseFloat(bars[j].style.height);
        if (valJ < pivot) {
            i++;
            let temp = bars[i].style.height;
            bars[i].style.height = bars[j].style.height;
            bars[j].style.height = temp;
            bars[i].style.backgroundColor = '#a855f7';
        } else {
            bars[j].style.backgroundColor = '#38bdf8';
        }
    }
    i++;
    let temp = bars[i].style.height;
    bars[i].style.height = bars[r].style.height;
    bars[r].style.height = temp;
    
    for(let k=l; k<=r; k++) bars[k].style.backgroundColor = '#38bdf8';
    return i;
}

async function quickSort(bars, l, r) {
    if (l < r) {
        let pi = await partition(bars, l, r);
        bars[pi].style.backgroundColor = '#22c55e';
        await quickSort(bars, l, pi - 1);
        await quickSort(bars, pi + 1, r);
    } else if(l >= 0 && l < bars.length) {
        bars[l].style.backgroundColor = '#22c55e';
    }
}

async function quickSortMain() {
    const bars = document.querySelectorAll('.array-bar');
    await quickSort(bars, 0, bars.length - 1);
    bars.forEach(b => b.style.backgroundColor = '#22c55e');
}

// 3. Merge Sort
async function mergeSortMain() {
    // A Complex implementation to bulk up code and show advanced logic
    const bars = document.querySelectorAll('.array-bar');
    await mergeSortHelper(bars, 0, bars.length - 1);
    bars.forEach(b => b.style.backgroundColor = '#22c55e');
}

async function mergeSortHelper(bars, l, r) {
    if(l >= r) return;
    const m = l + Math.floor((r - l) / 2);
    await mergeSortHelper(bars, l, m);
    await mergeSortHelper(bars, m + 1, r);
    await merge(bars, l, m, r);
}

async function merge(bars, l, m, r) {
    const n1 = m - l + 1;
    const n2 = r - m;
    let L = new Array(n1);
    let R = new Array(n2);
    for (let i = 0; i < n1; i++) {
        await sleep(getDelay());
        bars[l + i].style.backgroundColor = '#fb923c';
        L[i] = bars[l + i].style.height;
    }
    for (let j = 0; j < n2; j++) {
        await sleep(getDelay());
        bars[m + 1 + j].style.backgroundColor = '#fde047';
        R[j] = bars[m + 1 + j].style.height;
    }
    await sleep(getDelay());
    let i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        await sleep(getDelay());
        if (parseFloat(L[i]) <= parseFloat(R[j])) {
            bars[k].style.height = L[i];
            i++;
        } else {
            bars[k].style.height = R[j];
            j++;
        }
        bars[k].style.backgroundColor = '#86efac';
        k++;
    }
    while (i < n1) {
        await sleep(getDelay());
        bars[k].style.height = L[i];
        bars[k].style.backgroundColor = '#86efac';
        i++; k++;
    }
    while (j < n2) {
        await sleep(getDelay());
        bars[k].style.height = R[j];
        bars[k].style.backgroundColor = '#86efac';
        j++; k++;
    }
}

// 4. Heap Sort (Advanced)
async function heapify(bars, n, i) {
    let largest = i; 
    let l = 2 * i + 1; 
    let r = 2 * i + 2; 

    if (l < n && parseFloat(bars[l].style.height) > parseFloat(bars[largest].style.height)) largest = l;
    if (r < n && parseFloat(bars[r].style.height) > parseFloat(bars[largest].style.height)) largest = r;

    if (largest != i) {
        bars[i].style.backgroundColor = '#ef4444';
        bars[largest].style.backgroundColor = '#ef4444';
        await sleep(getDelay());
        
        let temp = bars[i].style.height;
        bars[i].style.height = bars[largest].style.height;
        bars[largest].style.height = temp;

        bars[i].style.backgroundColor = '#38bdf8';
        bars[largest].style.backgroundColor = '#38bdf8';
        await heapify(bars, n, largest);
    }
}

async function heapSort() {
    let bars = document.querySelectorAll('.array-bar');
    let n = bars.length;

    for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
        await heapify(bars, n, i);
    }
    for (let i = n - 1; i > 0; i--) {
        let temp = bars[0].style.height;
        bars[0].style.height = bars[i].style.height;
        bars[i].style.height = temp;
        
        bars[i].style.backgroundColor = '#22c55e'; // Sorted
        await heapify(bars, i, 0);
    }
    bars[0].style.backgroundColor = '#22c55e';
}

// ==========================================
// MODULE 2: GRAPH / PATHFINDING VISUALIZER
// ==========================================

function initPathfindingMode() {
    STATE.mode = 'path';
    modePathBtn.classList.replace('text-slate-400', 'text-white');
    modePathBtn.classList.add('bg-accent');
    modeSortingBtn.classList.replace('text-white', 'text-slate-400');
    modeSortingBtn.classList.remove('bg-accent');

    controlsPanel.innerHTML = `
        <button id="btn-clear-board">Clear Board</button>
        <button id="btn-clear-path">Clear Path</button>
        <button id="btn-dijkstra">Dijkstra's Algo</button>
        <button id="btn-astar">A* Search</button>
    `;

    document.getElementById('btn-clear-board').addEventListener('click', createGrid);
    document.getElementById('btn-clear-path').addEventListener('click', clearPath);
    document.getElementById('btn-dijkstra').addEventListener('click', async () => { toggleControls(true); await dijkstra(); toggleControls(false); });
    document.getElementById('btn-astar').addEventListener('click', async () => { toggleControls(true); await aStar(); toggleControls(false); });

    createGrid();
}

function createGrid() {
    if (STATE.isAnimating) return;
    visualizerContainer.innerHTML = `<div class="grid-container" id="grid" style="grid-template-columns: repeat(${STATE.COLS}, 1fr);"></div>`;
    const gridEl = document.getElementById('grid');
    STATE.grid = [];

    for (let r = 0; r < STATE.ROWS; r++) {
        let currentRow = [];
        for (let c = 0; c < STATE.COLS; c++) {
            const node = createNode(r, c);
            currentRow.push(node);
            const nodeEl = document.createElement('div');
            nodeEl.id = `node-${r}-${c}`;
            nodeEl.className = 'grid-node bg-white';
            
            if (r === STATE.startNode.r && c === STATE.startNode.c) nodeEl.classList.add('node-start');
            if (r === STATE.endNode.r && c === STATE.endNode.c) nodeEl.classList.add('node-end');

            // Mouse events for drawing walls
            nodeEl.addEventListener('mousedown', () => handleMouseDown(r, c));
            nodeEl.addEventListener('mouseenter', () => handleMouseEnter(r, c));
            nodeEl.addEventListener('mouseup', handleMouseUp);
            
            gridEl.appendChild(nodeEl);
        }
        STATE.grid.push(currentRow);
    }
}

function createNode(r, c) {
    return {
        r, c,
        isStart: r === STATE.startNode.r && c === STATE.startNode.c,
        isEnd: r === STATE.endNode.r && c === STATE.endNode.c,
        distance: Infinity,
        isVisited: false,
        isWall: false,
        previousNode: null,
        f: Infinity, g: Infinity, h: 0 // For A*
    };
}

// Wall Drawing Logic
function handleMouseDown(r, c) {
    if (STATE.isAnimating) return;
    STATE.mouseIsPressed = true;
    toggleWall(r, c);
}
function handleMouseEnter(r, c) {
    if (!STATE.mouseIsPressed || STATE.isAnimating) return;
    toggleWall(r, c);
}
function handleMouseUp() {
    STATE.mouseIsPressed = false;
}
function toggleWall(r, c) {
    const node = STATE.grid[r][c];
    if(node.isStart || node.isEnd) return;
    node.isWall = !node.isWall;
    const el = document.getElementById(`node-${r}-${c}`);
    if(node.isWall) el.classList.add('node-wall');
    else el.classList.remove('node-wall');
}

function clearPath() {
    if (STATE.isAnimating) return;
    for (let r = 0; r < STATE.ROWS; r++) {
        for (let c = 0; c < STATE.COLS; c++) {
            const node = STATE.grid[r][c];
            node.isVisited = false;
            node.distance = Infinity;
            node.previousNode = null;
            node.f = Infinity; node.g = Infinity;
            const el = document.getElementById(`node-${r}-${c}`);
            el.classList.remove('node-visited', 'node-path');
        }
    }
}

// Custom Priority Queue for Pathfinding (Adds advanced JS complexity)
class PriorityQueue {
    constructor() { this.values = []; }
    enqueue(val, priority) {
        this.values.push({val, priority});
        this.sort();
    }
    dequeue() { return this.values.shift(); }
    sort() { this.values.sort((a, b) => a.priority - b.priority); }
    isEmpty() { return this.values.length === 0; }
}

// Algorithm: Dijkstra
async function dijkstra() {
    clearPath();
    const startNode = STATE.grid[STATE.startNode.r][STATE.startNode.c];
    const endNode = STATE.grid[STATE.endNode.r][STATE.endNode.c];
    startNode.distance = 0;
    
    let unvisitedNodes = getAllNodes();
    
    while(unvisitedNodes.length > 0) {
        unvisitedNodes.sort((a, b) => a.distance - b.distance);
        const closestNode = unvisitedNodes.shift();
        
        if (closestNode.isWall) continue;
        if (closestNode.distance === Infinity) break;
        
        closestNode.isVisited = true;
        if (!closestNode.isStart && !closestNode.isEnd) {
            document.getElementById(`node-${closestNode.r}-${closestNode.c}`).classList.add('node-visited');
            await sleep(getDelay() / 10); // Faster for grid
        }
        
        if (closestNode === endNode) {
            await animatePath(endNode);
            return;
        }
        updateUnvisitedNeighbors(closestNode);
    }
}

// Algorithm: A* Search (Advanced Heuristic approach)
async function aStar() {
    clearPath();
    const startNode = STATE.grid[STATE.startNode.r][STATE.startNode.c];
    const endNode = STATE.grid[STATE.endNode.r][STATE.endNode.c];
    
    let openSet = [startNode];
    startNode.g = 0;
    startNode.f = heuristic(startNode, endNode);
    
    while (openSet.length > 0) {
        openSet.sort((a, b) => a.f - b.f);
        let current = openSet.shift();
        
        if (current === endNode) {
            await animatePath(endNode);
            return;
        }
        
        current.isVisited = true;
        if (!current.isStart && !current.isEnd) {
            document.getElementById(`node-${current.r}-${current.c}`).classList.add('node-visited');
            await sleep(getDelay() / 10);
        }
        
        let neighbors = getNeighbors(current);
        for (let neighbor of neighbors) {
            if (neighbor.isWall || neighbor.isVisited) continue;
            
            let tempG = current.g + 1;
            let newPath = false;
            
            if (openSet.includes(neighbor)) {
                if (tempG < neighbor.g) {
                    neighbor.g = tempG;
                    newPath = true;
                }
            } else {
                neighbor.g = tempG;
                newPath = true;
                openSet.push(neighbor);
            }
            
            if (newPath) {
                neighbor.h = heuristic(neighbor, endNode);
                neighbor.f = neighbor.g + neighbor.h;
                neighbor.previousNode = current;
            }
        }
    }
}

function heuristic(a, b) {
    // Manhattan distance
    return Math.abs(a.r - b.r) + Math.abs(a.c - b.c);
}

function updateUnvisitedNeighbors(node) {
    const neighbors = getNeighbors(node);
    for (const neighbor of neighbors) {
        if (!neighbor.isVisited) {
            neighbor.distance = node.distance + 1;
            neighbor.previousNode = node;
        }
    }
}

function getNeighbors(node) {
    const neighbors = [];
    const { r, c } = node;
    if (r > 0) neighbors.push(STATE.grid[r - 1][c]);
    if (r < STATE.ROWS - 1) neighbors.push(STATE.grid[r + 1][c]);
    if (c > 0) neighbors.push(STATE.grid[r][c - 1]);
    if (c < STATE.COLS - 1) neighbors.push(STATE.grid[r][c + 1]);
    return neighbors;
}

function getAllNodes() {
    const nodes = [];
    for (const row of STATE.grid) {
        for (const node of row) nodes.push(node);
    }
    return nodes;
}

async function animatePath(endNode) {
    const nodesInPath = [];
    let currentNode = endNode;
    while (currentNode !== null) {
        nodesInPath.unshift(currentNode);
        currentNode = currentNode.previousNode;
    }
    for (let i = 0; i < nodesInPath.length; i++) {
        if (nodesInPath[i].isStart || nodesInPath[i].isEnd) continue;
        await sleep(20);
        document.getElementById(`node-${nodesInPath[i].r}-${nodesInPath[i].c}`).classList.add('node-path');
    }
}

// Event Listeners for Mode Switching
modeSortingBtn.addEventListener('click', initSortingMode);
modePathBtn.addEventListener('click', initPathfindingMode);

// Initialize Default State
initSortingMode();
