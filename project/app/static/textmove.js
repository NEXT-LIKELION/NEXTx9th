let currentDroppable = null;
  
result.onmousedown = function(event) {

  let shiftX = event.clientX - result.getBoundingClientRect().left;
  let shiftY = event.clientY - result.getBoundingClientRect().top;

  result.style.position = 'absolute';
  result.style.zIndex = 1000;
  document.body.append(result);

  moveAt(event.pageX, event.pageY);

  function moveAt(pageX, pageY) {
    result.style.left = pageX - shiftX + 'px';
    result.style.top = pageY - shiftY + 'px';
  }

  function onMouseMove(event) {
    moveAt(event.pageX, event.pageY);
    console.log(event.clientX)
    console.log(event.clientY)

    result.hidden = true;
    let elemBelow = document.elementFromPoint(event.clientX, event.clientY);
    result.hidden = false;

    if (!elemBelow) return;

    let droppableBelow = elemBelow.closest('.droppable');
    if (currentDroppable != droppableBelow) {
      if (currentDroppable) { // null when we were not over a droppable before this event
        leaveDroppable(currentDroppable);
      }
      currentDroppable = droppableBelow;
      if (currentDroppable) { // null if we're not coming over a droppable now
        // (maybe just left the droppable)
        enterDroppable(currentDroppable);
      }
    }
  }

  document.addEventListener('click', onMouseMove);

  result.onmouseup = function() {
    document.removeEventListener('click', onMouseMove);
    result.onmouseup = null;
  };

};
result.ondragstart = function() {
  return false;
};