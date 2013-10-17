#    Copyright (C) 2013  Eric Koo <erickoo@umich.edu>
#    USE Lab, Digital Media Commons, University of Michigan Library
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see [http://www.gnu.org/licenses/].

import pydot

print 'Generating visualization of Coursera export tables...'
prog = 'sfdp' # twopi sfdp
graph = pydot.Dot(ranksep=2, ratio='auto')

# Define nodes
print '   Defining nodes...'
hash_mapping = []
hash_mapping.append("hash_mapping")

anonymized_forum = []
anonymized_forum.append("forum_forums")
anonymized_forum.append("forum_threads")
anonymized_forum.append("forum_posts")
anonymized_forum.append("forum_comments")
anonymized_forum.append("forum_reporting")
anonymized_forum.append("forum_reputation_record")
anonymized_forum.append("forum_reputation_points")
anonymized_forum.append("forum_subscribe_forums")
anonymized_forum.append("forum_subscribe_threads")
anonymized_forum.append("forum_tags")
anonymized_forum.append("forum_tags_threads")
anonymized_forum.append("activity_log")

anonymized_general = []
anonymized_general.append("access_groups")
anonymized_general.append("announcements")
anonymized_general.append("course_grades")
anonymized_general.append("late_days_applied")
anonymized_general.append("late_days_left")
anonymized_general.append("navbar_list")
anonymized_general.append("wiki_pages")
anonymized_general.append("wiki_revisions")
anonymized_general.append("users")
anonymized_general.append("sections")
anonymized_general.append("items_sections")
anonymized_general.append("quiz_metadata")
anonymized_general.append("quiz_submission_metadata")
anonymized_general.append("lecture_metadata")
anonymized_general.append("lecture_submission_metadata")
anonymized_general.append("assignment_metadata")
anonymized_general.append("assignment_part_metadata")
anonymized_general.append("assignment_submission_metadata")
anonymized_general.append("hg_assessment_metadata")
anonymized_general.append("hg_assessment_submission_metadata")
anonymized_general.append("hg_assessment_overall_evaluation_metadata")
anonymized_general.append("hg_assessment_evaluation_metadata")
anonymized_general.append("hg_assessment_calibration_gradings")
anonymized_general.append("hg_assessment_peer_grading_metadata")
anonymized_general.append("hg_assessment_peer_grading_set_metadata")
anonymized_general.append("hg_assessment_self_grading_set_metadata")
anonymized_general.append("hg_assessment_training_metadata")
anonymized_general.append("hg_assessment_training_set_metadata")

ids = []
ids.append("user_id")
ids.append("anon_user_id")
ids.append("forum_user_id")
ids.append("forum_id")
ids.append("thread_id")
ids.append("post_id")
ids.append("tag_id")
ids.append("item_id ('post')")
ids.append("item_id ('comment')")
ids.append("access_group_id")
ids.append("page_id")
ids.append("section_id")
ids.append("assignment_id")
ids.append("item_id ('quiz')")
ids.append("item_id ('lecture')")
ids.append("item_id ('assignment')")
ids.append("assessment_id")
ids.append("submission_id")
ids.append("evaluation_id")
ids.append("peer_grading_set_id")
ids.append("calibration_set_id")
ids.append("training_set_id")

# Render nodes
shape = "rect"
style = "filled"
fillcolor = "#D6D3D6"
penwidth = 2
fontname = "Courier"
for table in hash_mapping:
  node = pydot.Node(table, shape=shape, style=style, fillcolor=fillcolor, penwidth=penwidth, fontname=fontname)
  graph.add_node(node)

style = "filled"
fillcolor = "#D6D3D6"
penwidth = 2
for table in anonymized_forum:
  node = pydot.Node(table, shape=shape, style=style, fillcolor=fillcolor, penwidth=penwidth, fontname=fontname)
  graph.add_node(node)

style = "filled"
fillcolor = "#D6D3D6"
penwidth = 2
for table in anonymized_general:
  node = pydot.Node(table, shape=shape, style=style, fillcolor=fillcolor, penwidth=penwidth, fontname=fontname)
  graph.add_node(node)

shape = "none"
style = "none"
fillcolor = "none"
penwidth = 2
for table in ids:
  node = pydot.Node(table, shape=shape, style=style, fillcolor=fillcolor, penwidth=penwidth, fontname=fontname)
  graph.add_node(node)

# Define edges
print '   Defining edges...'
table_id = []
id_table = []

table_id.append(["hash_mapping","user_id"])
table_id.append(["hash_mapping","anon_user_id"])
table_id.append(["hash_mapping","forum_user_id"])

id_table.append(["forum_user_id","forum_threads"])
id_table.append(["forum_user_id","forum_posts"])
id_table.append(["forum_user_id","forum_comments"])
id_table.append(["forum_user_id","forum_reporting"])
id_table.append(["forum_user_id","forum_reputation_record"])
id_table.append(["forum_user_id","forum_reputation_points"])
id_table.append(["forum_user_id","forum_subscribe_forums"])
id_table.append(["forum_user_id","forum_subscribe_threads"])
id_table.append(["forum_user_id","activity_log"])

id_table.append(["anon_user_id","announcements"])
id_table.append(["anon_user_id","course_grades"])
id_table.append(["anon_user_id","late_days_applied"])
id_table.append(["anon_user_id","late_days_left"])
id_table.append(["anon_user_id","wiki_revisions"])
id_table.append(["anon_user_id","users"])
id_table.append(["anon_user_id","quiz_submission_metadata"])
id_table.append(["anon_user_id","lecture_submission_metadata"])
id_table.append(["anon_user_id","assignment_submission_metadata"])
id_table.append(["anon_user_id","hg_assessment_metadata"])
id_table.append(["anon_user_id","hg_assessment_submission_metadata"])
id_table.append(["anon_user_id","hg_assessment_evaluation_metadata"])
id_table.append(["anon_user_id","hg_assessment_peer_grading_set_metadata"])
id_table.append(["anon_user_id","hg_assessment_self_grading_set_metadata"])
id_table.append(["anon_user_id","hg_assessment_training_set_metadata"])

table_id.append(["forum_forums","forum_id"])
table_id.append(["forum_threads","thread_id"])
table_id.append(["forum_posts","post_id"])
table_id.append(["forum_posts","item_id ('post')"])
table_id.append(["forum_comments","item_id ('comment')"])
table_id.append(["forum_tags","tag_id"])

id_table.append(["forum_id","forum_threads"])
id_table.append(["forum_id","forum_subscribe_forums"])
id_table.append(["thread_id","forum_posts"])
id_table.append(["thread_id","forum_subscribe_threads"])
id_table.append(["thread_id","forum_tags_threads"])
id_table.append(["post_id","forum_comments"])
id_table.append(["item_id ('post')","forum_reporting"])
id_table.append(["item_id ('comment')","forum_reporting"])
id_table.append(["tag_id","forum_tags_threads"])

table_id.append(["access_groups","access_group_id"])
table_id.append(["wiki_pages","page_id"])
table_id.append(["sections","section_id"])
table_id.append(["quiz_metadata","item_id ('quiz')"])
table_id.append(["lecture_metadata","item_id ('lecture')"])
table_id.append(["assignment_part_metadata","item_id ('assignment')"])
table_id.append(["assignment_metadata","assignment_id"])

id_table.append(["access_group_id","users"])
id_table.append(["page_id","wiki_revisions"])
id_table.append(["section_id","items_sections"])
id_table.append(["item_id ('quiz')","quiz_submission_metadata"])
id_table.append(["item_id ('quiz')","late_days_applied"])
id_table.append(["item_id ('quiz')","items_sections"])
id_table.append(["item_id ('lecture')","lecture_submission_metadata"])
id_table.append(["item_id ('lecture')","late_days_applied"])
id_table.append(["item_id ('lecture')","items_sections"])
id_table.append(["assignment_id","assignment_part_metadata"])
id_table.append(["item_id ('assignment')","assignment_submission_metadata"])
id_table.append(["item_id ('assignment')","late_days_applied"])
id_table.append(["item_id ('assignment')","items_sections"])

table_id.append(["hg_assessment_metadata","assessment_id"])
table_id.append(["hg_assessment_submission_metadata","submission_id"])
table_id.append(["hg_assessment_evaluation_metadata","evaluation_id"])
table_id.append(["hg_assessment_peer_grading_set_metadata","peer_grading_set_id"])
table_id.append(["hg_assessment_self_grading_set_metadata","calibration_set_id"])
table_id.append(["hg_assessment_training_set_metadata","training_set_id"])

id_table.append(["assessment_id","hg_assessment_submission_metadata"])
id_table.append(["assessment_id","hg_assessment_peer_grading_set_metadata"])
id_table.append(["assessment_id","hg_assessment_self_grading_set_metadata"])
id_table.append(["assessment_id","hg_assessment_training_set_metadata"])
id_table.append(["submission_id","hg_assessment_overall_evaluation_metadata"])
id_table.append(["submission_id","hg_assessment_evaluation_metadata"])
id_table.append(["evaluation_id","hg_assessment_calibration_gradings"])
id_table.append(["evaluation_id","hg_assessment_peer_grading_metadata"])
id_table.append(["evaluation_id","hg_assessment_training_metadata"])
id_table.append(["peer_grading_set_id","hg_assessment_peer_grading_metadata"])
id_table.append(["calibration_set_id","hg_assessment_calibration_gradings"])
id_table.append(["training_set_id","hg_assessment_training_metadata"])

# Render edges
shape = "normal"
penwidth = 1
color = "#333333"
for ref in table_id:
  edge = pydot.Edge(ref[0], ref[1], shape=shape, penwidth=penwidth, color=color)
  graph.add_edge(edge)

shape = "normal"
for ref in id_table:
  edge = pydot.Edge(ref[0], ref[1], shape=shape, penwidth=penwidth, color=color)
  graph.add_edge(edge)
print ''

# Output to .png
filename = 'export_tables_map.png'
print 'Writing to: '+filename
print 'Processing...'
graph.write_png(filename)
print 'Done.'
print ''
print ''
close = raw_input('Press any key to close this window.')
