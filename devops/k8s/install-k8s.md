# 安装 Kubernetes

1. OS 配置

   - 关闭防火墙
   - 关闭 swap
   - 关闭 SELinux
   - 安装 containerd
   - 安装
     - kubeadm: 初始化集群
     - kubelet: 用来启动和管理容器
     - kubectl: 与集群通信的命令行工具

2. kubeadm 初始化

   - init.yaml

   ```bash
   kubeadm config images pull --config init.yaml # 下载镜像
   kubeadm init --config=init.yaml --upload-certs # 初始化集群
   ```

   - etcd
     - 堆叠 etcd: service or static pod
     - 外部 etcd
   - flannel.yaml(网络插件未部署前，coredns 状态为 pending)`
   - coredns

3. 如何删除一个 k8s 节点

```bash
kubectl drain node-name --delete-emptydir-data --force --ignore-daemonsets
```
