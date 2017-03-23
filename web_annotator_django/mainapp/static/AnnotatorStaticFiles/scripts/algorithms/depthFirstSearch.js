//Returns Stack of valid neighbours
function getNeighbours(imgW, imgH, pnt, visited_points){
  valid_neighbs_stack = new Stack();
  if(pnt == null){
    return valid_neighbs_stack;
  }
  if(pnt.x + 1 < imgW){
    tmp_pnt = new Point(pnt.x + 1, pnt.y);
    if(!visited_points.visited(tmp_pnt)){
      valid_neighbs_stack.push(tmp_pnt);
    }
    if(pnt.y + 1 < imgH){
      tmp_pnt = new Point(pnt.x + 1, pnt.y + 1);
      if(!visited_points.visited(tmp_pnt)){
        valid_neighbs_stack.push(tmp_pnt);
      }      
    }
    if(pnt.y - 1 > 0){
      tmp_pnt = new Point(pnt.x + 1, pnt.y - 1);
      if(!visited_points.visited(tmp_pnt)){
        valid_neighbs_stack.push(tmp_pnt);
      }         
    }    
  }
  if(pnt.x - 1 > 0){
    tmp_pnt = new Point(pnt.x - 1, pnt.y);
    if(!visited_points.visited(tmp_pnt)){
      valid_neighbs_stack.push(tmp_pnt);
    } 
    if(pnt.y + 1 < imgH){
      tmp_pnt = new Point(pnt.x - 1, pnt.y + 1);
      if(!visited_points.visited(tmp_pnt)){
        valid_neighbs_stack.push(tmp_pnt);
      }       
    }    
    if(pnt.y - 1 > 0){
      tmp_pnt = new Point(pnt.x - 1, pnt.y - 1);
      if(!visited_points.visited(tmp_pnt)){
        valid_neighbs_stack.push(tmp_pnt);
      }        
    }
  }
  if(pnt.y + 1 < imgH){
    tmp_pnt = new Point(pnt.x, pnt.y + 1);
    if(!visited_points.visited(tmp_pnt)){
      valid_neighbs_stack.push(tmp_pnt);
    }    
  }
  if(pnt.y - 1 > 0){
    tmp_pnt = new Point(pnt.x, pnt.y - 1);
    if(!visited_points.visited(tmp_pnt)){
      valid_neighbs_stack.push(tmp_pnt);
    }      
  }
  return valid_neighbs_stack;
}

//col = x , row = y
function getRedPixelAt(img_data,pnt, imgW){
  return img_data[pnt.x*4 + pnt.y*imgW*4];
}

function findConnectedComponentRect(img_data, threshold, selected_point, imgW, imgH){ 
  //Init dss
  const dfs_stack = new Stack();
  dfs_stack.push(selected_point);
  var visited_points = new VisitHashMap();
  var top_margin = selected_point.y;
  var bottom_margin = selected_point.y;  
  var left_margin = selected_point.x;
  var right_margin = selected_point.x;

  visited_points.visit(selected_point);

  function expandSearch(pnt,father_pnt){
    if(!visited_points.visited[pnt]){
      visited_points.visit(pnt);
      if(Math.abs(getRedPixelAt(img_data, pnt, imgW) - getRedPixelAt(img_data, selected_point, imgW)) <= threshold){
        dfs_stack.push(pnt);

        //Margin Check
        if(pnt.x > right_margin){
          right_margin = pnt.x;
        }
        if(pnt.x < left_margin){
          left_margin = pnt.x;
        }   
        if(pnt.y > bottom_margin){
          bottom_margin = pnt.y;
        }
        if(pnt.y < top_margin){
          top_margin = pnt.y;
        }
      }
    }      
  }

  console.log(getRedPixelAt(img_data, selected_point, imgW));

  if(getRedPixelAt(img_data, selected_point, imgW) > 50){
    return {"top": 0, "bottom": 0, "left": 0, "right":0};
  }

  var max_iterations = 700;
  while(!dfs_stack.isEmpty() && max_iterations > 0){
    cur_pnt = dfs_stack.pop();
    neighbour_pts = getNeighbours(imgW, imgH, cur_pnt, visited_points);
    while(!neighbour_pts.isEmpty()){
      expandSearch(neighbour_pts.pop(), cur_pnt);
    }
    max_iterations--;
  }
  return {"top": top_margin, "bottom": bottom_margin, "left": left_margin, "right":right_margin};
}