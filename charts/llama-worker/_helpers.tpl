{{- define "app.container.name" -}}
{{ .Chart.Name }}-{{ .Values.name | default "app" }}-{{ .Release.Name }}
{{- end -}}