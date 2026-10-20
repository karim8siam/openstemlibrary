/**
 * Preserve the full bibliographic citation while removing links to
 * /references/<slug> endpoints that are NOT actually published.
 *
 * This module does not invent a reference URL or claim that a textbook has
 * been externally reviewed; a non-clickable citation is better than a 404.
 */
'use strict';
const internalCitationLink=/<a\b[^>]*\bhref\s*=\s*(["'])https:\/\/(?:www\.)?openstemlibrary\.com\/references\/([a-z0-9-]+)\1[^>]*>([\s\S]*?)<\/a>/gi;
function normalizeUnpublishedReferences(html,referenceExists=()=>false) {
  let normalizedCount=0;
  const output=html.replace(internalCitationLink,(whole,quote,slug,citation)=>{
    if(referenceExists(slug))return whole;
    normalizedCount++;
    return '<cite class="reader-reference-citation">'+citation+'</cite>';
  });
  return {html:output,normalizedCount};
}
module.exports={normalizeUnpublishedReferences};
