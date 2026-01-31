#!/usr/bin/env bash
set -e

# shellcheck disable=SC1091
source /home/rc2/jwt/rc/autostart/common_env.sh

# 免密 sudo 的 CAN 初始化（你之前已经配了 sudoers 的话）
sudo /usr/local/sbin/setup_can0.sh

LOCALIZER_GREP="localizer"   # 用来匹配 ros2 node list 里的名字关键词
MAX_WAIT=120

echo "[serial] waiting localizer node grep: ${LOCALIZER_GREP} ..."
deadline=$((SECONDS+MAX_WAIT))
while true; do
  if ros2 node list 2>/dev/null | grep -qi "${LOCALIZER_GREP}"; then
    echo "[serial] localizer node found."
    break
  fi

  if [ $SECONDS -ge $deadline ]; then
    echo "[serial] ERROR: localizer node not found after ${MAX_WAIT}s, still trying..."
    deadline=$((SECONDS+MAX_WAIT))
  fi

  sleep 1
done

# 按你说的：localizer起来后再等2秒再启动后续
sleep 4

exec ros2 service call /localizer/relocalize_check interface/srv/IsValid "{code: 0}"
