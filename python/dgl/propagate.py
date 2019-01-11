"""Module for message propagation."""
from __future__ import absolute_import

from . import traversal as trv

__all__ = ['prop_nodes', 'prop_nodes_bfs', 'prop_nodes_topo',
           'prop_edges', 'prop_edges_dfs']

def prop_nodes(graph,
               nodes_generator,
               message_func='default',
               reduce_func='default',
               apply_node_func='default'):
    """Functional method for :func:`dgl.DGLGraph.prop_nodes`.

    Parameters
    ----------
    node_generators : generator
        The generator of node frontiers.
    message_func : callable, optional
        The message function.
    reduce_func : callable, optional
        The reduce function.
    apply_node_func : callable, optional
        The update function.

    See Also
    --------
    dgl.DGLGraph.prop_nodes
    """
    graph.prop_nodes(nodes_generator, message_func, reduce_func, apply_node_func)

def prop_edges(graph,
               edges_generator,
               message_func='default',
               reduce_func='default',
               apply_node_func='default'):
    """Functional method for :func:`dgl.DGLGraph.prop_edges`.

    Parameters
    ----------
    edges_generator : generator
        The generator of edge frontiers.
    message_func : callable, optional
        The message function.
    reduce_func : callable, optional
        The reduce function.
    apply_node_func : callable, optional
        The update function.

    See Also
    --------
    dgl.DGLGraph.prop_edges
    """
    graph.prop_edges(edges_generator, message_func, reduce_func, apply_node_func)

def prop_nodes_bfs(graph,
                   source,
                   reverse=False,
                   message_func='default',
                   reduce_func='default',
                   apply_node_func='default'):
    """Message propagation using node frontiers generated by BFS.

    Parameters
    ----------
    graph : DGLGraph
        The graph object.
    source : list, tensor of nodes
        Source nodes.
    reverse : bool, optional
        If true, traverse following the in-edge direction.
    message_func : callable, optional
        The message function.
    reduce_func : callable, optional
        The reduce function.
    apply_node_func : callable, optional
        The update function.

    See Also
    --------
    dgl.traversal.bfs_nodes_generator
    """
    nodes_gen = trv.bfs_nodes_generator(graph, source, reverse)
    prop_nodes(graph, nodes_gen, message_func, reduce_func, apply_node_func)

def prop_nodes_topo(graph,
                    reverse=False,
                    message_func='default',
                    reduce_func='default',
                    apply_node_func='default'):
    """Message propagation using node frontiers generated by topological order.

    Parameters
    ----------
    graph : DGLGraph
        The graph object.
    reverse : bool, optional
        If true, traverse following the in-edge direction.
    message_func : callable, optional
        The message function.
    reduce_func : callable, optional
        The reduce function.
    apply_node_func : callable, optional
        The update function.

    See Also
    --------
    dgl.traversal.topological_nodes_generator
    """
    nodes_gen = trv.topological_nodes_generator(graph, reverse)
    prop_nodes(graph, nodes_gen, message_func, reduce_func, apply_node_func)

def prop_edges_dfs(graph,
                   source,
                   reverse=False,
                   has_reverse_edge=False,
                   has_nontree_edge=False,
                   message_func='default',
                   reduce_func='default',
                   apply_node_func='default'):
    """Message propagation using edge frontiers generated by labeled DFS.

    Parameters
    ----------
    graph : DGLGraph
        The graph object.
    source : list, tensor of nodes
        Source nodes.
    reverse : bool, optional
        If true, traverse following the in-edge direction.
    message_func : callable, optional
        The message function.
    reduce_func : callable, optional
        The reduce function.
    apply_node_func : callable, optional
        The update function.

    See Also
    --------
    dgl.traversal.dfs_labeled_edges_generator
    """
    edges_gen = trv.dfs_labeled_edges_generator(
        graph, source, reverse, has_reverse_edge, has_nontree_edge,
        return_labels=False)
    prop_edges(graph, edges_gen, message_func, reduce_func, apply_node_func)
