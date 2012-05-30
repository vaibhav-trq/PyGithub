# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
import GithubException
from DefaultValueForOptionalParameters import DefaultValueForOptionalParameters
import CommitFile
import NamedUser
import GitCommit
import CommitStats
import Commit
import CommitComment

class Commit( object ):
    def __init__( self, requester, attributes, completed ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )
        self.__completed = completed

    @property
    def author( self ):
        self.__completeIfNeeded( self.__author )
        return self.__author

    @property
    def commit( self ):
        self.__completeIfNeeded( self.__commit )
        return self.__commit

    @property
    def committer( self ):
        self.__completeIfNeeded( self.__committer )
        return self.__committer

    @property
    def files( self ):
        self.__completeIfNeeded( self.__files )
        return self.__files

    @property
    def parents( self ):
        self.__completeIfNeeded( self.__parents )
        return self.__parents

    @property
    def sha( self ):
        self.__completeIfNeeded( self.__sha )
        return self.__sha

    @property
    def stats( self ):
        self.__completeIfNeeded( self.__stats )
        return self.__stats

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    def create_comment( self, body, line = DefaultValueForOptionalParameters, path = DefaultValueForOptionalParameters, position = DefaultValueForOptionalParameters ):
        assert isinstance( body, ( str, unicode ) ), body
        if line is not DefaultValueForOptionalParameters:
            assert isinstance( line, int ), line
        if path is not DefaultValueForOptionalParameters:
            assert isinstance( path, ( str, unicode ) ), path
        if position is not DefaultValueForOptionalParameters:
            assert isinstance( position, int ), position
        post_parameters = {
            "body": body,
        }
        if line is not DefaultValueForOptionalParameters:
            post_parameters[ "line" ] = line
        if path is not DefaultValueForOptionalParameters:
            post_parameters[ "path" ] = path
        if position is not DefaultValueForOptionalParameters:
            post_parameters[ "position" ] = position
        status, headers, data = self.__requester.request(
            "POST",
            str( self.url ) + "/comments",
            None,
            post_parameters
        )
        if self.__requester.isFailureStatus( status ): # pragma no branch
            raise GithubException.GithubException( status, data ) # pragma no cover
        return CommitComment.CommitComment( self.__requester, data, completed = True )

    def get_comments( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/comments",
            None,
            None
        )
        if self.__requester.isFailureStatus( status ): # pragma no branch
            raise GithubException.GithubException( status, data ) # pragma no cover
        return PaginatedList.PaginatedList(
            CommitComment.CommitComment,
            self.__requester,
            headers,
            data
        )

    def __initAttributes( self ):
        self.__author = None
        self.__commit = None
        self.__committer = None
        self.__files = None
        self.__parents = None
        self.__sha = None
        self.__stats = None
        self.__url = None

    def __completeIfNeeded( self, testedAttribute ):
        if not self.__completed and testedAttribute is None:
            self.__complete() # pragma: no cover

    def __complete( self ): # pragma: no cover
        status, headers, data = self.__requester.request(
            "GET",
            self.__url,
            None,
            None
        )
        self.__useAttributes( data )
        self.__completed = True

    def __useAttributes( self, attributes ):
        if "author" in attributes and attributes[ "author" ] is not None: # pragma no branch
            assert isinstance( attributes[ "author" ], dict ), attributes[ "author" ]
            self.__author = NamedUser.NamedUser( self.__requester, attributes[ "author" ], completed = False )
        if "commit" in attributes and attributes[ "commit" ] is not None: # pragma no branch
            assert isinstance( attributes[ "commit" ], dict ), attributes[ "commit" ]
            self.__commit = GitCommit.GitCommit( self.__requester, attributes[ "commit" ], completed = False )
        if "committer" in attributes and attributes[ "committer" ] is not None: # pragma no branch
            assert isinstance( attributes[ "committer" ], dict ), attributes[ "committer" ]
            self.__committer = NamedUser.NamedUser( self.__requester, attributes[ "committer" ], completed = False )
        if "files" in attributes and attributes[ "files" ] is not None: # pragma no branch
            assert all( isinstance( element, dict ) for element in attributes[ "files" ] ), attributes[ "files" ]
            self.__files = [
                CommitFile.CommitFile( self.__requester, element, completed = False )
                for element in attributes[ "files" ]
            ]
        if "parents" in attributes and attributes[ "parents" ] is not None: # pragma no branch
            assert all( isinstance( element, dict ) for element in attributes[ "parents" ] ), attributes[ "parents" ]
            self.__parents = [
                Commit( self.__requester, element, completed = False )
                for element in attributes[ "parents" ]
            ]
        if "sha" in attributes and attributes[ "sha" ] is not None: # pragma no branch
            assert isinstance( attributes[ "sha" ], ( str, unicode ) ), attributes[ "sha" ]
            self.__sha = attributes[ "sha" ]
        if "stats" in attributes and attributes[ "stats" ] is not None: # pragma no branch
            assert isinstance( attributes[ "stats" ], dict ), attributes[ "stats" ]
            self.__stats = CommitStats.CommitStats( self.__requester, attributes[ "stats" ], completed = False )
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self.__url = attributes[ "url" ]
