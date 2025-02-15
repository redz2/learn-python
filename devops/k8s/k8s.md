#

## 组件

1. apiserver
   - keepalived + haproxy 保证高可用
2. controller manager
   - 通过选举方式产生领导者，其他节点处于 backup 状态(--leader-elect=true)
   - 如何查看 controller manager 日志？
3. scheduler
   - 通过选举方式产生领导者，其他节点处于 backup 状态(--leader-elect=true)

## Pod
