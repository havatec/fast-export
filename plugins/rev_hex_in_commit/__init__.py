def build_filter(args):
    return Filter(args)

class Filter:
    def __init__(self, args):
        pass

    def commit_message_filter(self, commit_data, ctx):
        #commit_data['desc'] = ( b'hg%d %s\n\n[ hg-changeset: %d:%s ]' % (ctx['rev'], commit_data['desc'], ctx['rev'], ctx['hex']))
        commit_data['desc'] = ( b'%s\n\n[ hg-changeset: %d:%s ]' % (commit_data['desc'], ctx['rev'], ctx['hex']))
