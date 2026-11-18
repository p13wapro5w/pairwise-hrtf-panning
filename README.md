# pairwise-hrtf-panning

戴耳机时声音从左后方跑到右前方、上下分不清、快速转头声像跳：HRTF 用球坐标固定；仰角不参与；头部转动没补偿；双耳延迟按距离；near-field 不处理；混响和 HRTF 顺序错；采样率不同滤波器不同；多人声源共用滤波器；耳廓模型按性别固定；HRTF 切换有爆音。audio/hrtf_panning.py 是核心，tests/test_hrtf_panning.py 15个红。要修的是：球坐标+仰角；头部转动补偿；双耳延迟；near-field；先 HRTF 后混响；采样率重采样；声源独立滤波；耳廓个性化；交叉淡入；爆音抑制。

## 运行

```bash
python -m pytest tests -q
```

初始状态：15 个用例失败。修复实现使全部用例通过，不要修改 `tests/` 下的测试。

子方向：音视频处理；任务类型：Bugfix；语言/框架：Python 3, pytest；环境可复现等级：无外部依赖。
