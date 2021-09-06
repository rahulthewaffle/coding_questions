# Binary bomb defusal:
# 
# Part of a crack team of bomb defusal specialists
# You're in charge of writing some code to handle bombs made by ACME co.
# 
# All of the bombs come with a set of switches (either on or off). Bombs are defused when 
# all of the switches reach the "target" state.
#
# However, ACME doesn't want you defusing bombs that easily, so if the bomb ever leaves a
# set of "SAFE" states, then the bomb will explode. These safe states are shared across 
# all the bombs you'll encounter.
#
# Your job, if you choose to accept it (and potentially get this job), is to write a 
# function which tells you whether you can defuse the a bomb or not.

State = list[bool]

SAFE_STATES: Set[State] = [...]
  
components: Dict[State, Int] = build_equiv_classes()

def build_equiv_classes():
  components = {}
  
  unused_states = SAFE_STATES.copy()
  last_component = 0
  while unused_states:
    component = last_component
    last_component += 1
    queue = deque()
    queue.enqueue(unused_states.pop())
    while queue:
      curr = queue.dequeue()
      components[curr] = component
      for state in generateAdj(curr):
      	if state not in unused_states:
          continue
        queue.enqueue(state)
        unused_states.remove(state)
  return components

def can_defuse(current: State, target: State) -> bool:
  return components[current] == components[target]

def can_defuse_nondynamic(current: List[bool], target: List[bool]) -> bool:
  safe_states = SAFE_STATES.copy()
  processing_queue = deque()
  processing_queue.enqueue(current)
  
  while processing_queue:
    cursor = processing_queue.pop()
    
    adjacent_states = generateAdj(cursor)
    
    for state in adjacent_states:
      if state not in safe_states:
        continue
      
      if state == target:
        return True
        
      processing_queue.enqueue(state)
      safe_states.remove(state)
        
	return False

def generateAdj(a: List[bool]) -> Generator(List[bool], None, None):
  for i in range(en(a)):
    b = a.flip_bit(i)
    yield b