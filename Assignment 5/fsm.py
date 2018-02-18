#! /usr/bin/python
"""
Name:           Cameron Padua
Class:          CSS390
Assignment:     Finite State Machine Generator
Description:    This script is used to generate C++ code using python. The
                user must provide all the edges, header, footer, and states
                to create a python file to run.

"""

class State(object):
    def __init__(self, name, action, edges):
        self.name = name
        self.action = action
        self.edges = edges


class Edge(object):
    def __init__(self, name, new_state, action):
        self.event = name
        self.new_state = new_state
        self.action = action


class Machine(object):
    def __init__(self, name):
        self.name = name
        self.the_header = ""
        self.the_footer = ""
        self.states = {}
        self.state_names = list()
        self.events = set()

    def header(self, text):
        self.the_header = text

    def footer(self, text):
        self.the_footer = text

    def state(self, name, action="", edges=None):
        if name in self.states:
            raise ValueError("duplicate state " + name)
        self.state_names.append(name)
        self.states[name] = State(name, action, edges)


    def edges(self, *args_list):
        Edges = []
        for arg in args_list:
            Edges.append(self.edge(arg[0], arg[1]))
        return Edges

    def edge(self, name, new_state, action=""):
        self.events.add(name)
        return Edge(name, new_state, action)

    def gen_state(self, state_name):
        state = self.states[state_name]
        print "             case {}_STATE:".format(state_name)
        print "                 cerr << \"state {}\" << endl;".format(state_name)
        print "                 " + state.action
        print "                 event = event_get_next_event();"
        print "                 cerr << \"event \" << EVENT_NAMES[event] << endl;".format(state_name)

        self.gen_events(state)

        print
        print  "                  default:"
        print "                     cerr << \"INVALID EVENT \" << event << " \
              "\" in state {} \" << endl;".format(state_name)
        print "                     return -1;"
        print "                   }"
        print "                   break;"

    def gen_events(self, state):
        print "                 switch (event) {"
        edges = state.edges
        if (edges == None): return
        for edge in edges:
            print
            print "                     case {}_EVENT".format(edge.event)
            print
            print "                         state = {}_STATE;".format(
                edge.new_state)
            print "                         break;"

    def gen(self):
        print self.the_header
        print """
    
#include <iostream>
using namespace std;
    
   
    """

        print "enum State {"
        for name in self.state_names:
            print "     {}_STATE,".format(name)
            # print " ", name, ","
        print "};"

        print "enum Event {"
        for name in self.events:
            print "     {}_EVENT,".format(name)
        print "     INVALID_EVENT"
        print "};"

        print "const char * EVENT_NAMES[] = {"
        for name in self.events:
            print "     \"{}\",".format(name)
        print "};"

        print "Event get_next_event();"

        print

        print "Event string_to_event(string event_string) {"
        for event in self.events:
            print ' if (event_string == "{ev}") {{return {ev}_EVENT;}}'.format(ev=event)
        print " return INVALID_EVENT;"
        print "}"

        print "int {}(State initial_state) {{".format(self.name)
        print " State state = initial_state;"
        print " Event event;"
        print " while (true) {"
        print "     switch (state) {"
        print

        for state in self.state_names:
            self.gen_state(state)

        print"          }"
        print"      }"
        print"  }"
        print self.the_footer