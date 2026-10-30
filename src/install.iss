#define App "Hashify"
#define Version "1.0.2"
#define Publisher "zzylenn"
#define AppURL "https://github.com/zzylenn/hashify"

[Setup]
AppId={{3F62BC9C-24BD-4195-BA82-9D52624619BA}
AppName={#App}
AppVersion={#Version}
AppPublisher={#Publisher}
AppPublisherURL={#AppURL}
AppSupportURL={#AppURL}
AppUpdatesURL={#AppURL}
DefaultDirName={autopf}\Hashify
DefaultGroupName=Hashify
UninstallDisplayIcon={app}\hashify.exe
LicenseFile=..\LICENSE
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
PrivilegesRequired=admin
DisableProgramGroupPage=yes
OutputBaseFilename=hashify-setup
SolidCompression=yes
WizardStyle=modern dynamic windows11
ChangesEnvironment=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: ".\dist\hashify.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Hashify"; Filename: "{app}\hashify.exe"

[Registry]
Root: HKLM; Subkey: "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"; ValueType: expandsz; ValueName: "Path"; ValueData: "{olddata};{app}"; Check: NeedsAddPath(ExpandConstant('{app}')); Flags: preservestringtype

[Code]
function NeedsAddPath(Param: string): Boolean;
var
  ExistingPath: string;
begin
  if not RegQueryStringValue(HKEY_LOCAL_MACHINE,
    'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
    'Path', ExistingPath) then
    ExistingPath := '';

  Result := Pos(';' + Lowercase(Param) + ';',
    ';' + Lowercase(ExistingPath) + ';') = 0;
end;

procedure RemoveHashifyFromPath();
var
  ExistingPath, NewPath, Entry: string;
  StartPos, EndPos: Integer;
begin
  if not RegQueryStringValue(HKEY_LOCAL_MACHINE,
    'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
    'Path', ExistingPath) then
    Exit;

  NewPath := '';
  ExistingPath := ExistingPath + ';';
  StartPos := 1;

  while StartPos <= Length(ExistingPath) do
  begin
    EndPos := StartPos;
    while (EndPos <= Length(ExistingPath)) and
      (ExistingPath[EndPos] <> ';') do
      EndPos := EndPos + 1;

    Entry := Copy(ExistingPath, StartPos, EndPos - StartPos);

    if CompareText(RemoveQuotes(Entry), ExpandConstant('{app}')) <> 0 then
    begin
      if NewPath <> '' then
        NewPath := NewPath + ';';
      NewPath := NewPath + Entry;
    end;

    StartPos := EndPos + 1;
  end;

  RegWriteExpandStringValue(HKEY_LOCAL_MACHINE,
    'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
    'Path', NewPath);
end;

procedure CurUninstallStepChanged(CurUninstallStep: TUninstallStep);
begin
  if CurUninstallStep = usUninstall then
    RemoveHashifyFromPath();
end;