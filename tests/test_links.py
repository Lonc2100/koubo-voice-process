from pathlib import Path
import re,unittest
class Links(unittest.TestCase):
 def test_relative_links(self):
  r=Path(__file__).resolve().parents[1]
  for f in r.rglob('*.md'):
   for x in re.findall(r'\]\(([^)]+)\)',f.read_text('utf8')):
    if not x.startswith(('http','#','mailto:')): self.assertTrue((f.parent/x).is_file(),(f,x))
