#####
# 重点
#####
import q84_largest_rectangle_in_histogram
import q30_substring_with_concatenation_of_all_words
import q31_next_permutation
import q32_longest_valid_parentheses
import q74_search_2D_matrix
import q97_interleaving_string
# 乘积 -> 维护候选值 
# 遇到0怎么办?
import tq152_max_prod_subarray 

# 接雨水: 
# 双端指针: 如何移动指针? 当前指针位置能接多少水? -> 维护最长木板
# 单调栈: 弹出的索引位置与当前位置之间能接多少水? -> 利用单调性
import tq42_trapping_rain_water

# 找零
# dfs/dp: 常规状态记忆; 只需要最短路径 -> 借助bfs寻找最短/提前停止
import tq322_coin_change

#####
# 列表
#####

import q82_remove_duplicates_ii

# 时刻注意数组越界问题
import q25_reverse_nodes_in_k_group
import q20_valid_parenthesis

# 链表+环 思路
# 快慢指针解决 +1 /2 问题
import q147_insertion_sort_list
import q142_linked_list_cycle
import q148_sort_list

# 桶
import q164_maximum_gap

# KMP
import q28_first_occurrence_in_a_string

# 排序与自定义比较
import q179_largest_number

##### 
# 集合
#####

# 求集合->去重的思路: 记录之前的值? bisect_left/right?
import q15_3_sum
import q39_combination_sum
import q40_combination_sum_II
# 为什么要排序? 提前终止, 节省标记
import q47_permutations_ii
# 重点, 回顾思路

# 并查集
import q128_longest_consecutive_seq
import q130_surrounded_regions

#####
# 二分\分治
#####
import q57_insert_interval
# 重做反思

#####
# 动态规划
#####

# 状态转移
import q53_maximum_subarray
import q174_dungeon_game
# 搞清楚状态转移是什么, 是否节约了时间
# 重点回顾这道题!!!
import q72_edit_distance

# 回溯
import q131_palindrome_partitioning
# 重点回顾: 从两个方向考虑回溯填表
import q132_palindrome_partitioning_ii
# 重点仍然是填表的顺序, 如何填表是合理的?
# 定位瓶颈并针对优化
# 总的来说这道题局限于回文的特点

import q87_scramble_string

# 经典最大状态转移
import tq312_burst_balloons

# 重点
import q115_distinct_subseq
import q188_buy_sell_stock_iv
# 重点回顾!!!
import tq309_buy_sell_stock_with_cooldown

#####
# 图
#####

# bfs, 回溯与前驱
import q126_word_ladder_ii

# 二分图
# 判断二分图/二分图的性质: 奇环/染色
import q886_possible_bipartition

# 匹配 最大流

#####
# HOT 100
#####

# tq169_majority_element 寻找出现次数超出n/2的元素 -> 对消
# tq198_house_robber 不能抢相邻房子 -> 保存多个状态
# tq200_number_of_islands 01图连通性 -> dfs递归
# tq238_product_of_arr_except_self 不能使用除法 -> 前后缀思想, 需要考虑0么?
# tq647_palindromic_substrings 回文中心扩展
