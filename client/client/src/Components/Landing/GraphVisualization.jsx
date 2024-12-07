import React from "react";
import {ForceGraph2D} from "react-force-graph";
import { useNavigate } from "react-router-dom";

const GraphVisualization = ({ matrix, keys }) => {
  const navigate = useNavigate()
  const graphData = React.useMemo(() => {
    console.log(keys)
    const nodes = keys.map((key, i) => ({ id: key, popularity: matrix[i][i] }));

    const links = [];
    for (let i = 0; i < matrix.length; i++) {
      for (let j = 0; j < matrix[i].length; j++) {
        if (i !== j && matrix[i][j] > 0) {
          links.push({
            source: keys[i],
            target: keys[j],
            value: matrix[i][j],
          });
        }
      }
    }

    return { nodes, links };
  }, [matrix, keys]);

  const globalEdgeScale = 700;
  const globalNodeScale = 25;

  return (
    <ForceGraph2D
      graphData={graphData}
      nodeAutoColorBy="id"
      linkWidth={(link) => link.value / globalEdgeScale}
      nodeCanvasObject={(node, ctx, globalScale) => {
        const label = node.id;
        const fontSize = 12 / globalScale;
        ctx.font = `${fontSize}px Sans-Serif`;
        ctx.fillStyle = node.color || "black";

        const radius = Math.sqrt(node.popularity) / globalNodeScale;
        ctx.beginPath();
        ctx.arc(node.x, node.y, radius, 0, 2 * Math.PI, false);
        ctx.fill();

        ctx.fillText(label, node.x + radius + 2, node.y + fontSize / 2);
        
      }}
      onNodeClick={(node) => {
        navigate(`/${node.id}`);
      }}
      width={1400}
      height={600}
    />
  );
};

export default GraphVisualization
