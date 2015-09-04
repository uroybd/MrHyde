package org.faudroids.mrhyde.github;

import java.util.List;

import retrofit.http.GET;
import retrofit.http.Query;

/**
 * Retrofit interface for fetching emails from GitHub.
 *
 * Fixes a bug in the
 * <href a="https://github.com/eclipse/egit-github/blob/master/org.eclipse.egit.github.core/src/org/eclipse/egit/github/core/service/UserService.java#L402">egit core lib</href>.
 * GitHub API does not return a list of strings, but rather a list of objects when fetching emails.
 */
public interface GitHubEmailsApi {

	@GET("/user/emails")
	List<Email> getEmails(@Query("access_token") String token);

}
