
���c�[���i�[�ꏊ
  https://pjshr170.soln.jp/IJS90B0/ln/lib/O8Fkrpq
  12.STEP2.5  \10_�R���g���[��\90_���p��\phase5_NSO���J��\30_�����[�X�񎦕�\ping-ssh�ڑ��m�FTool\
   ��pingChkTool.zip   : ping�ڑ��m�F�c�[��
   ��sshChkTool.zip    : ssh�ڑ��m�F�c�[��

���c�[������C���[�W
  ===================================
 �E��L�̃c�[���upingChkTool.zip�v�usshChkTool.zip�v���e�T�[�o��
   �z�u���Ď��s���܂��B
 �EF�X���n�A���p���Ŏg�p����ꍇ�́upingChk.list�v�usshChk.list�v���X�V����
   �g�p���ĉ������B
  ===================================

���c�[�����s���@
  ------------------------------------------------------------
  1.�c�[���z�u
    �c�[�����s����T�[�o�ɁA�upingChkTool.zip�v�usshChkTool.zip�v��
    �z�u����B

  2.�c�[���W�J
    # TOOLPUT_DIR="/tmp"
      ���c�[����z�u�����f�B���N�g���ɍ��킹��B

    # cd ${TOOLPUT_DIR}
    # ls -l pingChkTool.zip sshChkTool.zip
      ���t�@�C�������݂��邱�Ƃ��m�F����B

    # unzip pingChkTool.zip
    # unzip sshChkTool.zip
      ���c�[�����W�J����邱�Ƃ��m�F����B


  3.ping�ڑ��c�[�����s
    # cd pingChkTool
    # vim pingChk.list
      ��ping�ݒ�t�@�C�������������m�F����B
    # /bin/bash pingChkExe.sh
      ��ping�ڑ���NG�ƂȂ������̂�W���o�͂��܂��B
      ���ڂ����͓��f�B���N�g���́uREADME.txt�v���Q�ƁB

  4.ssh�ڑ��c�[�����s
    # cd ${TOOLPUT_DIR}/sshChkTool
    # vim sshChk.list
      ��ssh�ݒ�t�@�C�������������m�F����B
    # python sshChkExe.py
      ��SSH�ڑ���NG�ƂȂ������̂�W���o�͂��܂��B
      ���ڂ����͓��f�B���N�g���́uREADME.txt�v���Q�ƁB
  ------------------------------------------------------------

���c�[���폜���@
  ------------------------------------------------------------
  1.�c�[���폜
    # TOOLPUT_DIR="/tmp"
      ���c�[����z�u�����f�B���N�g���ɍ��킹��B
    # cd ${TOOLPUT_DIR}
    # ls -l pingChkTool.zip sshChkTool.zip
    # ls -ld pingChkTool sshChkTool
      ���t�@�C�������݂��邱�Ƃ��m�F����B
    
    # rm -f pingChkTool.zip sshChkTool.zip
    # rm -rf pingChkTool sshChkTool

    # ls -l pingChkTool.zip sshChkTool.zip
    # ls -ld pingChkTool sshChkTool
      ���t�@�C�����폜����Ă��邱�Ƃ��m�F
  ------------------------------------------------------------

