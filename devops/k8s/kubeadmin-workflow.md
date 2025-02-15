# Kubeadmin Workflow

1. preflight: 检查
   - 内核版本
   - crgoups 模块
   - kubeadme 和 kubelet 版本
   - 端口
   - ip, mount 命令
   - containerd 是否安装
2. certs: 生成证书
   - k8s 中的各种服务都需要 HTTPS 访问，包括 apiserver, etcd, kubelet
     - 用户通过 kubectl 获取容器日志时，需要 apiserver 向 kubelet 发送请求
3. kubeconfig: 生成 kubeconfig 文件 (访问 apiserver 时需要)
   - admin.conf
   - kubelet.conf
   - controller-manager.conf
   - scheduler.conf
4. control-plane: 安装控制平面
   - generate static pod manifests
   - kubelet 启动时会自动检查 /etc/kubernetes/manifests（kubelet 地位很高）
5. etcd: apiserver 使用
   - Generate static Pod manifest file for local etcd
6. upload-config: 上传配置
7. mark-control-plane: 标记为控制平面节点
8. bootstrap-token: 用来添加节点
