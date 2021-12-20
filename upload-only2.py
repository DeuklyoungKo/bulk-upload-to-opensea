# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IHRraW50ZXIKaW1wb3J0IHN1YnByb2Nlc3MKZnJvbSB0a2ludGVyIGltcG9ydCAqCmZyb20gdGtpbnRlciBpbXBvcnQgZmlsZWRpYWxvZwppbXBvcnQgdGtpbnRlciBhcyB0awpmcm9tIHRraW50ZXIgaW1wb3J0IG1lc3NhZ2Vib3gKaW1wb3J0IHRraW50ZXIuZm9udCBhcyBmb250CmZyb20gUElMIGltcG9ydCBJbWFnZVRrLCBJbWFnZQppbXBvcnQgdXJsbGliLnJlcXVlc3QKZnJvbSBpbyBpbXBvcnQgQnl0ZXNJTwppbXBvcnQgb3MKaW1wb3J0IGlvCmltcG9ydCBzeXMKaW1wb3J0IHBpY2tsZQppbXBvcnQgdGltZQpmcm9tIGRlY2ltYWwgaW1wb3J0ICoKaW1wb3J0IHdlYmJyb3dzZXIKZnJvbSBzZWxlbml1bSBpbXBvcnQgd2ViZHJpdmVyCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLmNvbW1vbi5ieSBpbXBvcnQgQnkKZnJvbSBzZWxlbml1bS53ZWJkcml2ZXIuc3VwcG9ydC53YWl0IGltcG9ydCBXZWJEcml2ZXJXYWl0CmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLmNocm9tZS5vcHRpb25zIGltcG9ydCBPcHRpb25zCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLnN1cHBvcnQgaW1wb3J0IGV4cGVjdGVkX2NvbmRpdGlvbnMgYXMgRXhwZWN0ZWRDb25kaXRpb25zCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLnN1cHBvcnQudWkgaW1wb3J0IFNlbGVjdAppbXBvcnQganNvbiAKCmZyb20gQ1NWIGltcG9ydCBDU1YKZnJvbSBKU09OIGltcG9ydCBKU09OCmZyb20gTkZUIGltcG9ydCBORlQKCgpyb290ID0gVGsoKQoKcm9vdC5nZW9tZXRyeSgnNzUweDc1MCcpCnJvb3QucmVzaXphYmxlKEZhbHNlLCBGYWxzZSkKcm9vdC50aXRsZSgiTkZUcyBVcGxvYWQgdG8gT3BlblNlYSB2MS4wIikKICAKaW5wdXRfc2F2ZV9saXN0ID0gWyJORlRzIGZvbGRlciA6IiwgMCwgMCwgMCwgMCwgMCwgMCwgMCwgMF0KbWFpbl9kaXJlY3RvcnkgPSBvcy5wYXRoLmpvaW4oc3lzLnBhdGhbMF0pCgoKZGVmIHN1cHBvcnRVUkwoKToKICAgIHdlYmJyb3dzZXIub3Blbl9uZXcoImh0dHBzOi8vd3d3LmluZm90cmV4Lm5ldC9vcGVuc2VhL3N1cHBvcnQuYXNwP3I9YXBwIikKCgpjbGFzcyBXZWJJbWFnZToKICAgIGRlZiBfX2luaXRfXyhzZWxmLCB1cmwpOgogICAgICAgIHdpdGggdXJsbGliLnJlcXVlc3QudXJsb3Blbih1cmwpIGFzIHU6CiAgICAgICAgICAgIHJhd19kYXRhID0gdS5yZWFkKCkKICAgICAgICAjc2VsZi5pbWFnZSA9IHRrLlBob3RvSW1hZ2UoZGF0YT1iYXNlNjQuZW5jb2RlYnl0ZXMocmF3X2RhdGEpKQogICAgICAgIGltYWdlID0gSW1hZ2Uub3Blbihpby5CeXRlc0lPKHJhd19kYXRhKSkKICAgICAgICBzZWxmLmltYWdlID0gSW1hZ2VUay5QaG90b0ltYWdlKGltYWdlKQoKICAgIGRlZiBnZXQoc2VsZik6CiAgICAgICAgcmV0dXJuIHNlbGYuaW1hZ2UKaW1hZ2V1cmwgPSAiaHR0cHM6Ly93d3cuaW5mb3RyZXgubmV0L29wZW5zZWEvaGVhZGVyLnBuZyIKaW1nID0gV2ViSW1hZ2UoaW1hZ2V1cmwpLmdldCgpCmltYWdlbGFiID0gdGsuTGFiZWwocm9vdCwgaW1hZ2U9aW1nKQppbWFnZWxhYi5ncmlkKHJvdz0wLCBjb2x1bW5zcGFuPTIpCmltYWdlbGFiLmJpbmQoIjxCdXR0b24tMT4iLCBsYW1iZGEgZTpzdXBwb3J0VVJMKCkpCgppc19wb2x5Z29uID0gQm9vbGVhblZhcigpCmlzX3BvbHlnb24uc2V0KEZhbHNlKSAKCmRlZiBvcGVuX2Nocm9tZV9wcm9maWxlKCk6CiAgICBzdWJwcm9jZXNzLlBvcGVuKAogICAgICAgIFsKICAgICAgICAgICAgInN0YXJ0IiwKICAgICAgICAgICAgImNocm9tZSIsCiAgICAgICAgICAgICItLXJlbW90ZS1kZWJ1Z2dpbmctcG9ydD04OTg5IiwKICAgICAgICAgICAgIi0tdXNlci1kYXRhLWRpcj0iICsgbWFpbl9kaXJlY3RvcnkgKyAiL2Nocm9tZV9wcm9maWxlIiwKICAgICAgICBdLAogICAgICAgIHNoZWxsPVRydWUsCiAgICApCgoKZGVmIHNhdmVfZmlsZV9wYXRoKCk6CiAgICAjcmV0dXJuIG9zLnBhdGguam9pbihzeXMucGF0aFswXSwgIlNhdmVfZmlsZS5jbG91ZCIpIAogICAgcmV0dXJuIG9zLnBhdGguam9pbihzeXMucGF0aFswXSwgIlNhdmVfZ3VpLmNsb3VkIikgCgoKIyBhc2sgZm9yIGRpcmVjdG9yeSBvbiBjbGlja2luZyBidXR0b24sIGNoYW5nZXMgYnV0dG9uIG5hbWUuCmRlZiB1cGxvYWRfZm9sZGVyX2lucHV0KCk6CiAgICBnbG9iYWwgdXBsb2FkX3BhdGgKICAgIHVwbG9hZF9wYXRoID0gZmlsZWRpYWxvZy5hc2tkaXJlY3RvcnkoKQogICAgTmFtZV9jaGFuZ2VfaW1nX2ZvbGRlcl9idXR0b24odXBsb2FkX3BhdGgpCgpkZWYgTmFtZV9jaGFuZ2VfaW1nX2ZvbGRlcl9idXR0b24odXBsb2FkX2ZvbGRlcl9pbnB1dCk6CiAgICB1cGxvYWRfZm9sZGVyX2lucHV0X2J1dHRvblsidGV4dCJdID0gdXBsb2FkX2ZvbGRlcl9pbnB1dAoKZGVmIGlzX251bWVyaWModmFsKToKCWlmIHN0cih2YWwpLmlzZGlnaXQoKToKCQlyZXR1cm4gVHJ1ZQoJZWxpZiBzdHIodmFsKS5yZXBsYWNlKCcuJywnJywxKS5pc2RpZ2l0KCk6CgkJcmV0dXJuIFRydWUKCWVsc2U6CgkJcmV0dXJuIEZhbHNlCgpjbGFzcyBJbnB1dEZpZWxkOgogICAgZGVmIF9faW5pdF9fKHNlbGYsIGxhYmVsLCByb3dfaW8sIGNvbHVtbl9pbywgcG9zLCAgbWFzdGVyPXJvb3QpOgogICAgICAgIHNlbGYubWFzdGVyID0gbWFzdGVyCiAgICAgICAgc2VsZi5pbnB1dF9maWVsZCA9IEVudHJ5KHNlbGYubWFzdGVyLCB3aWR0aD02MCkKICAgICAgICBzZWxmLmlucHV0X2ZpZWxkLmdyaWQoaXBhZHk9MykKICAgICAgICBzZWxmLmlucHV0X2ZpZWxkLmxhYmVsID0gTGFiZWwobWFzdGVyLCB0ZXh0PWxhYmVsLCBhbmNob3I9InciLCB3aWR0aD0yMCwgaGVpZ2h0PTEgKQogICAgICAgIHNlbGYuaW5wdXRfZmllbGQubGFiZWwuZ3JpZChyb3c9cm93X2lvLCBjb2x1bW49Y29sdW1uX2lvLCBwYWR4PTEyLCBwYWR5PTIpCiAgICAgICAgc2VsZi5pbnB1dF9maWVsZC5ncmlkKHJvdz1yb3dfaW8sIGNvbHVtbj1jb2x1bW5faW8gKyAxLCBwYWR4PTEyLCBwYWR5PTIpCiAgICAgICAgdHJ5OgogICAgICAgICAgICB3aXRoIG9wZW4oc2F2ZV9maWxlX3BhdGgoKSwgInJiIikgYXMgaW5maWxlOgogICAgICAgICAgICAgICAgbmV3X2RpY3QgPSBwaWNrbGUubG9hZChpbmZpbGUpCiAgICAgICAgICAgICAgICBzZWxmLmluc2VydF90ZXh0KG5ld19ka'
love = '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'
god = 'k5OSIpCiAgICAgICAgc3lzLmV4aXQoKQoKICAgIHByb2plY3RfcGF0aCA9IG1haW5fZGlyZWN0b3J5CiAgICBmaWxlX3BhdGggPSB1cGxvYWRfcGF0aAogICAgY29sbGVjdGlvbl9saW5rID0gY29sbGVjdGlvbl9saW5rX2lucHV0LmlucHV0X2ZpZWxkLmdldCgpCiAgICBzdGFydF9udW0gPSBpbnQoc3RhcnRfbnVtX2lucHV0LmlucHV0X2ZpZWxkLmdldCgpKQogICAgZW5kX251bSA9IGludChlbmRfbnVtX2lucHV0LmlucHV0X2ZpZWxkLmdldCgpKQogICAgbG9vcF9wcmljZSA9IGZsb2F0KHByaWNlLmlucHV0X2ZpZWxkLmdldCgpKQogICAgbG9vcF90aXRsZSA9IHRpdGxlLmlucHV0X2ZpZWxkLmdldCgpCiAgICBsb29wX2ZpbGVfZm9ybWF0ID0gZmlsZV9mb3JtYXQuaW5wdXRfZmllbGQuZ2V0KCkKICAgIGxvb3BfZXh0ZXJuYWxfbGluayA9IHN0cihleHRlcm5hbF9saW5rLmlucHV0X2ZpZWxkLmdldCgpKQogICAgbG9vcF9kZXNjcmlwdGlvbiA9IGRlc2NyaXB0aW9uLmlucHV0X2ZpZWxkLmdldCgpCgogICAgIyNjaHJvbWVvcHRpb25zCiAgICBvcHQgPSBPcHRpb25zKCkKICAgIG9wdC5hZGRfZXhwZXJpbWVudGFsX29wdGlvbigiZGVidWdnZXJBZGRyZXNzIiwgImxvY2FsaG9zdDo4OTg5IikKICAgIGRyaXZlciA9IHdlYmRyaXZlci5DaHJvbWUoCiAgICAgICAgZXhlY3V0YWJsZV9wYXRoPXByb2plY3RfcGF0aCArICIvY2hyb21lZHJpdmVyLmV4ZSIsCiAgICAgICAgY2hyb21lX29wdGlvbnM9b3B0LAogICAgKQogICAgd2FpdCA9IFdlYkRyaXZlcldhaXQoZHJpdmVyLCA2MCkKCiAgICAjIyN3YWl0IGZvciBtZXRob2RzCiAgICBkZWYgd2FpdF9jc3Nfc2VsZWN0b3IoY29kZSk6CiAgICAgICAgd2FpdC51bnRpbCgKICAgICAgICAgICAgRXhwZWN0ZWRDb25kaXRpb25zLnByZXNlbmNlX29mX2VsZW1lbnRfbG9jYXRlZCgoQnkuQ1NTX1NFTEVDVE9SLCBjb2RlKSkKICAgICAgICApCiAgICAgICAgCiAgICBkZWYgd2FpdF9jc3Nfc2VsZWN0b3JUZXN0KGNvZGUpOgogICAgICAgIHdhaXQudW50aWwoCiAgICAgICAgICAgIEV4cGVjdGVkQ29uZGl0aW9ucy5lbGVtZW50VG9CZUNsaWNrYWJsZSgoQnkuQ1NTX1NFTEVDVE9SLCBjb2RlKSkKICAgICAgICApICAgIAoKICAgIGRlZiB3YWl0X3hwYXRoKGNvZGUpOgogICAgICAgIHdhaXQudW50aWwoRXhwZWN0ZWRDb25kaXRpb25zLnByZXNlbmNlX29mX2VsZW1lbnRfbG9jYXRlZCgoQnkuWFBBVEgsIGNvZGUpKSkKCgogICAgd2hpbGUgZW5kX251bSA+PSBzdGFydF9udW06CiAgICAgICAgcHJpbnQoIlN0YXJ0IGNyZWF0aW5nIE5GVCAiICsgIGxvb3BfdGl0bGUgKyBzdHIoc3RhcnRfbnVtKSkKICAgICAgICBwcmludCgnbnVtYmVyICcsICBzdGFydF9udW0pCiAgICAgICAgZHJpdmVyLmdldChjb2xsZWN0aW9uX2xpbmspCgogICAgICAgIHdhaXRfeHBhdGgoJy8vKltAaWQ9Im1lZGlhIl0nKQogICAgICAgIGltYWdlVXBsb2FkID0gZHJpdmVyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnLy8qW0BpZD0ibWVkaWEiXScpCiAgICAgICAgaW1hZ2VQYXRoID0gb3MucGF0aC5hYnNwYXRoKGZpbGVfcGF0aCArICJcXGltYWdlc1xcIiArIHN0cihzdGFydF9udW0pICsgIi4iICsgbG9vcF9maWxlX2Zvcm1hdCkgICMgY2hhbmdlIGZvbGRlciBoZXJlCiAgICAgICAgaW1hZ2VVcGxvYWQuc2VuZF9rZXlzKGltYWdlUGF0aCkKICAgICAgICB0aW1lLnNsZWVwKDIpCgogICAgICAgIG5hbWUgPSBkcml2ZXIuZmluZF9lbGVtZW50X2J5X3hwYXRoKCcvLypbQGlkPSJuYW1lIl0nKQogICAgICAgIG5hbWUuc2VuZF9rZXlzKGxvb3BfdGl0bGUgKyBzdHIoc3RhcnRfbnVtKSkgICMgKzEwMDAgZm9yIG90aGVyIGZvbGRlcnMgI2NoYW5nZSBuYW1lIGJlZm9yZSAiIyIKICAgICAgICB0aW1lLnNsZWVwKDIpCgogICAgICAgIGV4dF9saW5rID0gZHJpdmVyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnLy8qW0BpZD0iZXh0ZXJuYWxfbGluayJdJykKICAgICAgICBleHRfbGluay5zZW5kX2tleXMobG9vcF9leHRlcm5hbF9saW5rKQogICAgICAgIHRpbWUuc2xlZXAoMikKCiAgICAgICAgZGVzYyA9IGRyaXZlci5maW5kX2VsZW1lbnRfYnlfeHBhdGgoJy8vKltAaWQ9ImRlc2NyaXB0aW9uIl0nKQogICAgICAgIGRlc2Muc2VuZF9rZXlzKGxvb3BfZGVzY3JpcHRpb24pCiAgICAgICAgdGltZS5zbGVlcCgxKQoKICAgICAgICAjanNvbkRhdGEgPSBKU09OKGZpbGVfcGF0aCArICIvanNvbi8iKyBzdHIoc3RhcnRfbnVtKSArICIuanNvbiIpLnJlYWRGcm9tRmlsZSgpCgogICAgICAgIGpzb25GaWxlID0gZmlsZV9wYXRoICsgIi9qc29uLyIrIHN0cihzdGFydF9udW0pICsgIi5qc29uIgogICAgICAgIGlmIG9zLnBhdGguaXNmaWxlKGpzb25GaWxlKSBhbmQgb3MuYWNjZXNzKGpzb25GaWxlLCBvcy5SX09LKToKICAgICAgICAgICAKICAgICAgICAgICAgI3ByaW50KHN0cihqc29uTWV0YURhdGEpKQogICAgICAgICAgICB3YWl0X2Nzc19zZWxlY3RvcigiYnV0dG9uW2FyaWEtbGFiZWw9J0FkZCBwcm9wZXJ0aWVzJ10iKQogICAgICAgICAgICBwcm9wZXJ0aWVzID0gZHJpdmVyLmZpbmRfZWxlbWVudF9ieV9jc3Nfc2VsZWN0b3IoImJ1dHRvblthcmlhLWxhYmVsPSdBZGQgcHJvcGVydGllcyddIikKICAgICAgICAgICAgZHJpdmVyLmV4ZWN1dGVfc2NyaXB0KCJhcmd1bWVudHNbMF0uY2xpY2soKTsiLCBwcm9wZXJ0aWVzKQogICAgICAgICAgICB0aW1lLnNsZWVwKDEpCgogICAgICAgICAgICAjIGpzb25EYXRhID0gSlNPTihvcy5nZXRjd2QoKSArICIvZGF0YS8iKyBzdHIoc3RhcnRfbnVtKSArICIuanNvbiIpLnJlYWRGcm9tRmlsZSgpCiAgICAgICAgICAgICMganNvbk1ldGFEYXRhID0ganNvbkRhdGFbJ2F0dHJpYnV0ZXMnXQoKICAgICAgICAgICAgICMgY2hlY2tzIGlmIGZpbGUgZXhpc3RzCiAgICAgICAgICAgIGpzb25EYXRhID0ganNvbi5sb2FkcyhvcGVuKGZpbGVfcGF0aCAgKyAiXFxqc29uXFwiKyBzdHIoc3RhcnRfbnVtKSArICIuanNvbiIpLnJlYWQoKSkKICAgICAgICAgICAganNvbk1ldGFEYXRhID0ganNvbkRhdGFbJ2F0dHJpYnV0ZXMnXQoKICAgICAgICAgICAgZm9yIGtleSBpbiBqc29uTWV0YURhdGE6CiAgICAgICAgICAgICAgICBpbnB1dDEgPSBkcml2ZXIuZmluZF9lbGV'
destiny = 'gMJ50K2W5K3ujLKEbXPpiY3Evo2E5J0OwoTSmpm0vDKAmMKEHpzScqUATo3WgYF1vo2E5Vy0iqUWooTSmqPtcKF90MSfkKF9xnKLiMTy2Y2yhpUI0WlxXVPNtVPNtVPNtVPNtVPNtVTyhpUI0ZvN9VTElnKMypv5znJ5xK2IfMJ1yoaEsLaysrUOuqTtbWl8iqTWiMUyoDTAfLKAmCFWOp3AyqSElLJy0p0Mipz0gYJWiMUxvKF90pygfLKA0XPyqY3ExJmWqY2Ecqv9xnKLinJ5jqKDaXDbtVPNtVPNtVPNtVPNtVPNtV3OlnJ50XUA0pvueMKyoW3ElLJy0K3E5pTHaKFxcPvNtVPNtVPNtVPNtVPNtVPNwpUWcoaDbp3ElXTgyrIfaqzSfqJHaKFxcPvNtVPNtVPNtVPNtVPNtVPOcoaO1qQRhp2IhMS9eMKymXUA0pvueMKyoW3ElLJy0K3E5pTHaKFxcPvNtVPNtVPNtVPNtVPNtVPOcoaO1qQVhp2IhMS9eMKymXUA0pvueMKyoW3MuoUIyW10cXDbtVPNtVPNtVPNtVPNtVPNtMUWcqzIlYzMcozEsMJkyoJIhqS9vrI94pTS0nPtaYl9vqKE0o25oqTI4qPtcCFWOMTDtoJ9lMFWqWlxhL2kcL2fbXDbtVPNtVPNtVPNtVPO0nJ1yYaAfMJIjXQRcPtbtVPNtVPNtVPNtVPOxpzy2MKVhMzyhMS9yoTIgMJ50K2W5K3ujLKEbXPpiY2W1qUEioyg0MKu0XPx9VyAuqzHvKFpcYzAfnJAeXPxXVPNtVPNtVPNtVPNtqTygMF5moTIypPtkXDbXVPNtVPNtVPNwVSAyoTIwqPODo2k5M29hVTWfo2AeL2uunJ4tnJLtLKOjoTywLJWfMDbtVPNtVPNtVTyzVTymK3OioUyao24hM2I0XPx6PvNtVPNtVPNtVPNtVTWfo2AeL2uunJ5sLaI0qT9hVQ0tMUWcqzIlYzMcozEsMJkyoJIhqPuPrF5LHRSHFPjtWl8iXygNnJD9Vy9sozI4qPWqY2EcqyfkKF9gLJyhY2Ecqv9xnKLip2IwqTyiov9xnKLiMz9loF9xnKMoA10iMTy2Y2EcqyflKFpcPvNtVPNtVPNtVPNtVTWfo2AeL2uunJ5sLaI0qT9hYzAfnJAeXPxXVPNtVPNtVPNtVPNtpT9frJqioy9vqKE0o25soT9wLKEco24tCFNaYl9mpTShJ25ipz1uoTy6MF1mpTSwMFtcVQ0tVx11oJWunFWqWjbtVPNtVPNtVPNtVPO3LJy0YaIhqTyfXRI4pTIwqTIxD29hMTy0nJ9hpl5jpzImMJ5wMI9iMy9yoTIgMJ50K2kiL2S0MJDbPvNtVPNtVPNtVPNtVPNtVPNbDaxhJSOOIRtfVUOioUyao25sLaI0qT9hK2kiL2S0nJ9hXFxcPvNtVPNtVPNtVPNtVUOioUyao25sLaI0qT9hVQ0tMUWcqzIlYzMcozEsMJkyoJIhqPtXVPNtVPNtVPNtVPNtVPNtVRW5YyuDDIEVYPOjo2k5M29hK2W1qUEioy9fo2AuqTyiovxXVPNtVPNtVPNtVPNtpT9frJqioy9vqKE0o24hL2kcL2fbXDbXPvNtVPNtVPNtL3WyLKEyVQ0tMUWcqzIlYzMcozEsMJkyoJIhqS9vrI94pTS0nPtaYl8dJ0OcMQ0vK19hMKu0Vy0iMTy2JmSqY21unJ4iMTy2Y2Ecqv9mMJA0nJ9hY2EcqyflKF9zo3WgY2Ecqv9xnKMoZI0ip3Ouov9vqKE0o24aXDbtVPNtVPNtVTElnKMypv5yrTIwqKEyK3AwpzyjqPtvLKWaqJ1yoaEmJmOqYzAfnJAeXPx7VvjtL3WyLKEyXDbtVPNtVPNtVUEcoJHhp2kyMKNbZFxXPvNtVPNtVPNtq2ScqS9wp3Asp2IfMJA0o3VbVzyoLKWcLF1fLJWyoQ0aD2kip2HaKFVcPvNtVPNtVPNtL3Wip3ZtCFOxpzy2MKVhMzyhMS9yoTIgMJ50K2W5K2Amp19mMJkyL3EipvtvnIgupzyuYJkuLzIfCFqQoT9mMFqqVvxXVPNtVPNtVPOwpz9mpl5woTywnltcPvNtVPNtVPNtqTygMF5moTIypPtkXDbXPvNtVPNtVPNtp3EupaEsoaIgVQ0tp3EupaEsoaIgVPftZDbtVPNtVPNtVUOlnJ50XPqBEyDtL3WyLKEco24tL29gpTkyqTIxVFpcPtbwVlZwV0WIISECGvOnG05SVlZwVlZwVjbXPzymHT9frJqiovN9VUEenJ50MKVhD2uyL2gvqKE0o24bpz9iqPjtqTI4qQ0aHT9frJqiovOPoT9wn2AbLJyhWljtqzSlCJymK3OioUyao24fVUqcMUEbCGD5YPOuozAbo3V9VapvXDccp1OioUyao24hM3WcMPulo3p9ZwNfVTAioUIgow0kXDc1pTkiLJEsMz9fMTIlK2yhpUI0K2W1qUEiovN9VUEenJ50MKVhDaI0qT9hXUWio3DfVUqcMUEbCGHjYPObMJyanUD9ZFjtVUEyrUD9VxSxMPOBEyEmVSIjoT9uMPOTo2kxMKVvYPOwo21gLJ5xCKIjoT9uMS9zo2kxMKWsnJ5jqKDcPaIjoT9uMS9zo2kxMKWsnJ5jqKEsLaI0qT9hYzqlnJDbpz93CGVkYPOwo2k1oJ49ZFjtpTSxrQ0lXDcipTIhK2Wlo3qmMKVtCFO0n2yhqTIlYxW1qUEiovulo290YPO3nJE0nQ01ZPjtnTIcM2u0CGRfVPO0MKu0CFWCpTIhVRAbpz9gMFOPpz93p2IlVvjtL29goJShMQ1ipTIhK2Abpz9gMI9jpz9znJkyXDcipTIhK2Wlo3qmMKVhM3WcMPulo3p9ZwZfVTAioUIgow0kYPOjLJE5CGVcPzW1qUEioy9mLKMyVQ0tqTgcoaEypv5PqKE0o24bpz9iqPjtq2yxqTt9AGNfVTuynJqbqQ0kYPNtqTI4qQ0vH2S2MFOHnTymVRMipz0vYPOwo21gLJ5xCKAuqzHcVNcvqKE0o25sp2S2MF5apzyxXUWiqm0lZvjtL29fqJ1hCGRfVUOuMUx9ZvxXLaI0qT9hK3A0LKW0VQ0tqTgcoaEypv5PqKE0o24bpz9iqPjtq2yxqTt9AQDfVTuynJqbqQ0lYPOvMm0vM3WyMJ4vYPOzMm0vq2ucqTHvYPO0MKu0CFWGqTSlqPVfVTAioJ1uozD9oJScoy9jpz9apzSgK2kio3NcPzW1qUEioy9mqTSlqSfaMz9hqPqqVQ0tMz9hqP5To250XUAcrzH9ZGNfVUqynJqbqQ0aLz9fMPpcPzW1qUEioy9mqTSlqP5apzyxXUWiqm0lAFjtL29fqJ1hCGRfVUOuMUx9ZvxXMz9iqTIlVQ0tqTgcoaEypv5PqKE0o24bpz9iqPjtnTIcM2u0CGHfVUqcMUEbCGLjYPO0MKu0CFqGpT9hp29lVUEbnKZtpUWinzIwqPOpovODoTIup2HtL2kcL2ftnTIlMFO0olOmqKOjo3W0VTMipvOgrFOipTIhp2IuVTAioTkyL3Eco24fKT4tM2y2MFOcqPOuVTkcqUEfMFOfo3MyVT9lVTqlLJVtnKDuVSEbLJ5eVUyiqF4aYPNtL29goJShMQ1mqKOjo3W0IIWZYPOlMJkcMJL9E1WCG1MSVPNcPzMio3Eypv5apzyxXUWiqm0mZFjtL29fqJ1hp3Ouow0lYPOjLJE4CGZkYPOjLJE5CGZkXDbXPaElrGbXVPNtVUqcqTtto3OyovumLKMyK2McoTIspTS0nPtcYPNvpzVvXFOuplOcozMcoTH6PvNtVPNtVPNtozI3K2EcL3DtCFOjnJAeoTHhoT9uMPucozMcoTHcPvNtVPNtVPNtM2kiLzSfVUIjoT9uMS9jLKEbPvNtVPNtVPNtGzSgMI9wnTShM2IsnJ1aK2MioTEypy9vqKE0o24bozI3K2EcL3EoZS0cPvNtVPNtVPNtqKOfo2SxK3OuqTttCFOhMKqsMTywqSfjKDcyrTAypUDtEzyfMH5iqRMiqJ5xEKWlo3V6PvNtVPOjLKAmPvZwVlZwDyIHIR9BVScCGxHtEH5RVlZwVlZwVjclo290Yz1unJ5fo29jXPxXVPNtVN=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))